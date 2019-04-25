/* -*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -*- */

/**
 * \file screen-private.h  Handling of monitor configuration
 *
 * Managing multiple monitors
 * This file contains structures and functions that handle
 * multiple monitors, including reading the current configuration
 * and available hardware, and applying it.
 *
 * This interface is private to mutter, API users should look
 * at MetaScreen instead.
 */

/*
 * Copyright (C) 2001 Havoc Pennington
 * Copyright (C) 2003 Rob Adams
 * Copyright (C) 2004-2006 Elijah Newren
 * Copyright (C) 2013 Red Hat Inc.
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 2 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, see <http://www.gnu.org/licenses/>.
 */

#ifndef META_MONITOR_MANAGER_PRIVATE_H
#define META_MONITOR_MANAGER_PRIVATE_H

#include <cogl/cogl.h>
#include <libgnome-desktop/gnome-pnp-ids.h>
#include <libupower-glib/upower.h>

#include "display-private.h"
#include <meta/screen.h>
#include "stack-tracker.h"
#include <meta/meta-monitor-manager.h>

#include "meta-display-config-shared.h"
#include "meta-dbus-display-config.h"
#include "meta-cursor.h"

typedef struct _MetaMonitorConfigManager MetaMonitorConfigManager;
typedef struct _MetaMonitorConfigStore MetaMonitorConfigStore;
typedef struct _MetaMonitorsConfig MetaMonitorsConfig;

typedef struct _MetaMonitor MetaMonitor;
typedef struct _MetaMonitorNormal MetaMonitorNormal;
typedef struct _MetaMonitorTiled MetaMonitorTiled;
typedef struct _MetaMonitorSpec MetaMonitorSpec;
typedef struct _MetaLogicalMonitor MetaLogicalMonitor;

typedef struct _MetaMonitorMode MetaMonitorMode;

typedef struct _MetaGpu MetaGpu;

typedef struct _MetaCrtc MetaCrtc;
typedef struct _MetaOutput MetaOutput;
typedef struct _MetaCrtcMode MetaCrtcMode;
typedef struct _MetaCrtcInfo MetaCrtcInfo;
typedef struct _MetaOutputInfo MetaOutputInfo;
typedef struct _MetaTileInfo MetaTileInfo;

#define META_MONITOR_MANAGER_MIN_SCREEN_WIDTH 640
#define META_MONITOR_MANAGER_MIN_SCREEN_HEIGHT 480

typedef enum _MetaMonitorManagerCapability
{
  META_MONITOR_MANAGER_CAPABILITY_NONE = 0,
  META_MONITOR_MANAGER_CAPABILITY_MIRRORING = (1 << 0),
  META_MONITOR_MANAGER_CAPABILITY_LAYOUT_MODE = (1 << 1),
  META_MONITOR_MANAGER_CAPABILITY_GLOBAL_SCALE_REQUIRED = (1 << 2)
} MetaMonitorManagerCapability;

/* Equivalent to the 'method' enum in org.gnome.Mutter.DisplayConfig */
typedef enum _MetaMonitorsConfigMethod
{
  META_MONITORS_CONFIG_METHOD_VERIFY = 0,
  META_MONITORS_CONFIG_METHOD_TEMPORARY = 1,
  META_MONITORS_CONFIG_METHOD_PERSISTENT = 2
} MetaMonitorsConfigMethod;

/* Equivalent to the 'layout-mode' enum in org.gnome.Mutter.DisplayConfig */
typedef enum _MetaLogicalMonitorLayoutMode
{
  META_LOGICAL_MONITOR_LAYOUT_MODE_LOGICAL = 1,
  META_LOGICAL_MONITOR_LAYOUT_MODE_PHYSICAL = 2
} MetaLogicalMonitorLayoutMode;

typedef enum
{
  META_MONITOR_TRANSFORM_NORMAL,
  META_MONITOR_TRANSFORM_90,
  META_MONITOR_TRANSFORM_180,
  META_MONITOR_TRANSFORM_270,
  META_MONITOR_TRANSFORM_FLIPPED,
  META_MONITOR_TRANSFORM_FLIPPED_90,
  META_MONITOR_TRANSFORM_FLIPPED_180,
  META_MONITOR_TRANSFORM_FLIPPED_270,
} MetaMonitorTransform;

/*
 * MetaCrtcInfo:
 *
 * A representation of a CRTC configuration, generated by
 * MetaMonitorConfigManager.
 */
struct _MetaCrtcInfo
{
  MetaCrtc                 *crtc;
  MetaCrtcMode             *mode;
  int                       x;
  int                       y;
  MetaMonitorTransform      transform;
  GPtrArray                *outputs;
};

/*
 * MetaOutputInfo:
 *
 * A representation of a connector configuration, generated by
 * MetaMonitorConfigManager.
 */
struct _MetaOutputInfo
{
  MetaOutput  *output;
  gboolean     is_primary;
  gboolean     is_presentation;
  gboolean     is_underscanning;
};

#define META_TYPE_MONITOR_MANAGER            (meta_monitor_manager_get_type ())
#define META_MONITOR_MANAGER(obj)            (G_TYPE_CHECK_INSTANCE_CAST ((obj), META_TYPE_MONITOR_MANAGER, MetaMonitorManager))
#define META_MONITOR_MANAGER_CLASS(klass)    (G_TYPE_CHECK_CLASS_CAST ((klass),  META_TYPE_MONITOR_MANAGER, MetaMonitorManagerClass))
#define META_IS_MONITOR_MANAGER(obj)         (G_TYPE_CHECK_INSTANCE_TYPE ((obj), META_TYPE_MONITOR_MANAGER))
#define META_IS_MONITOR_MANAGER_CLASS(klass) (G_TYPE_CHECK_CLASS_TYPE ((klass),  META_TYPE_MONITOR_MANAGER))
#define META_MONITOR_MANAGER_GET_CLASS(obj)  (G_TYPE_INSTANCE_GET_CLASS ((obj),  META_TYPE_MONITOR_MANAGER, MetaMonitorManagerClass))

G_DEFINE_AUTOPTR_CLEANUP_FUNC (MetaMonitorManager, g_object_unref)

struct _MetaMonitorManager
{
  MetaDBusDisplayConfigSkeleton parent_instance;

  MetaBackend *backend;

  /* XXX: this structure is very badly
     packed, but I like the logical organization
     of fields */

  gboolean in_init;
  unsigned int serial;

  MetaPowerSave power_save_mode;

  MetaLogicalMonitorLayoutMode layout_mode;

  int screen_width;
  int screen_height;

  GList *gpus;

  GList *monitors;

  GList *logical_monitors;
  MetaLogicalMonitor *primary_logical_monitor;

  int dbus_name_id;

  int persistent_timeout_id;

  MetaMonitorConfigManager *config_manager;

  GnomePnpIds *pnp_ids;
  UpClient *up_client;
  gboolean lid_is_closed;

  gulong experimental_features_changed_handler_id;

  MetaMonitorSwitchConfigType current_switch_config;
};

struct _MetaMonitorManagerClass
{
  MetaDBusDisplayConfigSkeletonClass parent_class;

  char* (*get_edid_file) (MetaMonitorManager *,
                          MetaOutput         *);
  GBytes* (*read_edid) (MetaMonitorManager *,
                        MetaOutput         *);

  gboolean (*is_lid_closed) (MetaMonitorManager *);

  void (*ensure_initial_config) (MetaMonitorManager *);

  gboolean (*apply_monitors_config) (MetaMonitorManager      *,
                                     MetaMonitorsConfig      *,
                                     MetaMonitorsConfigMethod ,
                                     GError                 **);

  void (*set_power_save_mode) (MetaMonitorManager *,
                               MetaPowerSave);

  void (*change_backlight) (MetaMonitorManager *,
                            MetaOutput         *,
                            int);

  void (*get_crtc_gamma) (MetaMonitorManager  *,
                          MetaCrtc            *,
                          gsize               *,
                          unsigned short     **,
                          unsigned short     **,
                          unsigned short     **);
  void (*set_crtc_gamma) (MetaMonitorManager *,
                          MetaCrtc           *,
                          gsize               ,
                          unsigned short     *,
                          unsigned short     *,
                          unsigned short     *);

  void (*tiled_monitor_added) (MetaMonitorManager *,
                               MetaMonitor        *);

  void (*tiled_monitor_removed) (MetaMonitorManager *,
                                 MetaMonitor        *);

  gboolean (*is_transform_handled) (MetaMonitorManager  *,
                                    MetaCrtc            *,
                                    MetaMonitorTransform);

  float (*calculate_monitor_mode_scale) (MetaMonitorManager *,
                                         MetaMonitor        *,
                                         MetaMonitorMode    *);

  float * (*calculate_supported_scales) (MetaMonitorManager          *,
                                         MetaLogicalMonitorLayoutMode ,
                                         MetaMonitor                 *,
                                         MetaMonitorMode             *,
                                         int                         *);

  MetaMonitorManagerCapability (*get_capabilities) (MetaMonitorManager *);

  gboolean (*get_max_screen_size) (MetaMonitorManager *,
                                   int                *,
                                   int                *);

  MetaLogicalMonitorLayoutMode (*get_default_layout_mode) (MetaMonitorManager *);
};

MetaBackend *       meta_monitor_manager_get_backend (MetaMonitorManager *manager);

void                meta_monitor_manager_setup (MetaMonitorManager *manager);

void                meta_monitor_manager_rebuild (MetaMonitorManager *manager,
                                                  MetaMonitorsConfig *config);
void                meta_monitor_manager_rebuild_derived (MetaMonitorManager *manager,
                                                          MetaMonitorsConfig *config);

int                 meta_monitor_manager_get_num_logical_monitors (MetaMonitorManager *manager);

GList *             meta_monitor_manager_get_logical_monitors (MetaMonitorManager *manager);

MetaLogicalMonitor *meta_monitor_manager_get_logical_monitor_from_number (MetaMonitorManager *manager,
                                                                          int                 number);

MetaLogicalMonitor *meta_monitor_manager_get_primary_logical_monitor (MetaMonitorManager *manager);

MetaLogicalMonitor *meta_monitor_manager_get_logical_monitor_at (MetaMonitorManager *manager,
                                                                 float               x,
                                                                 float               y);

MetaLogicalMonitor *meta_monitor_manager_get_logical_monitor_from_rect (MetaMonitorManager *manager,
                                                                        MetaRectangle      *rect);

MetaLogicalMonitor *meta_monitor_manager_get_logical_monitor_neighbor (MetaMonitorManager *manager,
                                                                       MetaLogicalMonitor *logical_monitor,
                                                                       MetaScreenDirection direction);

MetaMonitor *       meta_monitor_manager_get_primary_monitor (MetaMonitorManager *manager);

MetaMonitor *       meta_monitor_manager_get_laptop_panel (MetaMonitorManager *manager);

MetaMonitor *       meta_monitor_manager_get_monitor_from_spec (MetaMonitorManager *manager,
                                                                MetaMonitorSpec    *monitor_spec);

MetaMonitor *       meta_monitor_manager_get_monitor_from_connector (MetaMonitorManager *manager,
                                                                     const char         *connector);

GList *             meta_monitor_manager_get_monitors      (MetaMonitorManager *manager);

void                meta_monitor_manager_add_gpu (MetaMonitorManager *manager,
                                                  MetaGpu            *gpu);

GList *             meta_monitor_manager_get_gpus (MetaMonitorManager *manager);

void                meta_monitor_manager_get_screen_size   (MetaMonitorManager *manager,
                                                            int                *width,
                                                            int                *height);

void                meta_monitor_manager_confirm_configuration (MetaMonitorManager *manager,
                                                                gboolean            ok);

void               meta_output_parse_edid (MetaOutput *output,
                                           GBytes     *edid);
gboolean           meta_output_is_laptop  (MetaOutput *output);

gboolean           meta_monitor_manager_has_hotplug_mode_update (MetaMonitorManager *manager);
void               meta_monitor_manager_read_current_state (MetaMonitorManager *manager);
void               meta_monitor_manager_on_hotplug (MetaMonitorManager *manager);

gboolean           meta_monitor_manager_get_monitor_matrix (MetaMonitorManager *manager,
                                                            MetaMonitor        *monitor,
                                                            MetaLogicalMonitor *logical_monitor,
                                                            gfloat              matrix[6]);

void               meta_monitor_manager_tiled_monitor_added (MetaMonitorManager *manager,
                                                             MetaMonitor        *monitor);
void               meta_monitor_manager_tiled_monitor_removed (MetaMonitorManager *manager,
                                                               MetaMonitor        *monitor);

gboolean           meta_monitor_manager_is_transform_handled (MetaMonitorManager  *manager,
                                                              MetaCrtc            *crtc,
                                                              MetaMonitorTransform transform);

MetaMonitorsConfig * meta_monitor_manager_ensure_configured (MetaMonitorManager *manager);

void               meta_monitor_manager_update_logical_state (MetaMonitorManager *manager,
                                                              MetaMonitorsConfig *config);
void               meta_monitor_manager_update_logical_state_derived (MetaMonitorManager *manager,
                                                                      MetaMonitorsConfig *config);

gboolean           meta_monitor_manager_is_lid_closed (MetaMonitorManager *manager);

void               meta_monitor_manager_lid_is_closed_changed (MetaMonitorManager *manager);

gboolean           meta_monitor_manager_is_headless (MetaMonitorManager *manager);

float              meta_monitor_manager_calculate_monitor_mode_scale (MetaMonitorManager *manager,
                                                                      MetaMonitor        *monitor,
                                                                      MetaMonitorMode    *monitor_mode);

float *            meta_monitor_manager_calculate_supported_scales (MetaMonitorManager          *,
                                                                    MetaLogicalMonitorLayoutMode ,
                                                                    MetaMonitor                 *,
                                                                    MetaMonitorMode             *,
                                                                    int                         *);

gboolean           meta_monitor_manager_is_scale_supported (MetaMonitorManager          *manager,
                                                            MetaLogicalMonitorLayoutMode layout_mode,
                                                            MetaMonitor                 *monitor,
                                                            MetaMonitorMode             *monitor_mode,
                                                            float                        scale);

MetaMonitorManagerCapability
                   meta_monitor_manager_get_capabilities (MetaMonitorManager *manager);

gboolean           meta_monitor_manager_get_max_screen_size (MetaMonitorManager *manager,
                                                             int                *max_width,
                                                             int                *max_height);

MetaLogicalMonitorLayoutMode
                   meta_monitor_manager_get_default_layout_mode (MetaMonitorManager *manager);

MetaMonitorConfigManager *
                   meta_monitor_manager_get_config_manager (MetaMonitorManager *manager);

void meta_monitor_manager_rotate_monitor (MetaMonitorManager *manager);

void meta_monitor_manager_clear_output (MetaOutput *output);
void meta_monitor_manager_clear_mode (MetaCrtcMode *mode);
void meta_monitor_manager_clear_crtc (MetaCrtc *crtc);

/* Returns true if transform causes width and height to be inverted
   This is true for the odd transforms in the enum */
static inline gboolean
meta_monitor_transform_is_rotated (MetaMonitorTransform transform)
{
  return (transform % 2);
}

/* Returns true if transform involves flipping */
static inline gboolean
meta_monitor_transform_is_flipped (MetaMonitorTransform transform)
{
  return (transform >= META_MONITOR_TRANSFORM_FLIPPED);
}

#endif /* META_MONITOR_MANAGER_PRIVATE_H */
