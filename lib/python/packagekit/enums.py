# This file was autogenerated from ../../../lib/packagekit-glib2/pk-enum.c by enum-converter.py

class PackageKitEnum:
	exit = ( "unknown", "success", "failed", "cancelled", "key-required", "eula-required", "media-change-required", "killed", "need-untrusted", "cancelled-priority", "skip-transaction", "repair-required", )
	status = ( "unknown", "wait", "setup", "running", "query", "info", "refresh-cache", "remove", "download", "install", "update", "cleanup", "obsolete", "dep-resolve", "sig-check", "test-commit", "commit", "request", "finished", "cancel", "download-repository", "download-packagelist", "download-filelist", "download-changelog", "download-group", "download-updateinfo", "repackaging", "loading-cache", "scan-applications", "generate-package-list", "waiting-for-lock", "waiting-for-auth", "scan-process-list", "check-executable-files", "check-libraries", "copy-files", "run-hook", )
	role = ( "unknown", "cancel", "depends-on", "get-details", "get-details-local", "get-files-local", "get-files", "get-packages", "get-repo-list", "required-by", "get-update-detail", "get-updates", "install-files", "install-packages", "install-signature", "refresh-cache", "remove-packages", "repo-enable", "repo-set-data", "repo-remove", "resolve", "search-details", "search-file", "search-group", "search-name", "update-packages", "what-provides", "accept-eula", "download-packages", "get-distro-upgrades", "get-categories", "get-old-transactions", "repair-system", "upgrade-system", )
	error = ( "unknown", "out-of-memory", "no-cache", "no-network", "not-supported", "internal-error", "gpg-failure", "filter-invalid", "package-id-invalid", "transaction-error", "transaction-cancelled", "package-not-installed", "package-not-found", "package-already-installed", "package-download-failed", "group-not-found", "group-list-invalid", "dep-resolution-failed", "create-thread-failed", "repo-not-found", "cannot-remove-system-package", "process-kill", "failed-initialization", "failed-finalise", "failed-config-parsing", "cannot-cancel", "cannot-get-lock", "no-packages-to-update", "cannot-write-repo-config", "local-install-failed", "bad-gpg-signature", "missing-gpg-signature", "cannot-install-source-package", "repo-configuration-error", "no-license-agreement", "file-conflicts", "package-conflicts", "repo-not-available", "invalid-package-file", "package-install-blocked", "package-corrupt", "all-packages-already-installed", "file-not-found", "no-more-mirrors-to-try", "no-distro-upgrade-data", "incompatible-architecture", "no-space-on-device", "media-change-required", "not-authorized", "update-not-found", "cannot-install-repo-unsigned", "cannot-update-repo-unsigned", "cannot-get-filelist", "cannot-get-requires", "cannot-disable-repository", "restricted-download", "package-failed-to-configure", "package-failed-to-build", "package-failed-to-install", "package-failed-to-remove", "failed-due-to-running-process", "package-database-changed", "provide-type-not-supported", "install-root-invalid", "cannot-fetch-sources", "cancelled-priority", "unfinished-transaction", "lock-required", "repo-already-set", )
	restart = ( "unknown", "none", "system", "session", "application", "security-system", "security-session", )
	filter = ( "unknown", "none", "installed", "~installed", "devel", "~devel", "gui", "~gui", "free", "~free", "visible", "~visible", "supported", "~supported", "basename", "~basename", "newest", "~newest", "arch", "~arch", "source", "~source", "collections", "~collections", "application", "~application", "downloaded", "~downloaded", )
	group = ( "unknown", "accessibility", "accessories", "education", "games", "graphics", "internet", "office", "other", "programming", "multimedia", "system", "desktop-gnome", "desktop-kde", "desktop-xfce", "desktop-other", "publishing", "servers", "fonts", "admin-tools", "legacy", "localization", "virtualization", "power-management", "security", "communication", "network", "maps", "repos", "science", "documentation", "electronics", "collections", "vendor", "newest", )
	update_state = ( "unknown", "testing", "unstable", "stable", )
	info = ( "unknown", "installed", "available", "unavailable", "low", "normal", "important", "security", "bugfix", "enhancement", "blocked", "downloading", "updating", "installing", "removing", "cleanup", "obsoleting", "collection-installed", "collection-available", "finished", "reinstalling", "downgrading", "preparing", "decompressing", "untrusted", "trusted", )
	sig_type = ( "unknown", "gpg", )
	upgrade = ( "unknown", "stable", "unstable", )
	network = ( "unknown", "offline", "online", "wired", "wifi", "mobile", )
	media_type = ( "unknown", "cd", "dvd", "disc", )
	authorize_type = ( "unknown", "yes", "no", "interactive", )
	upgrade_kind = ( "unknown", "minimal", "default", "complete", )
	transaction_flag = ( "none", "only-trusted", "simulate", "only-download", "allow-reinstall", "just-reinstall", "allow-downgrade", )

# Constants

AUTHORIZE_INTERACTIVE = "interactive"
AUTHORIZE_NO = "no"
AUTHORIZE_UNKNOWN = "unknown"
AUTHORIZE_YES = "yes"
DISTRO_UPGRADE_STABLE = "stable"
DISTRO_UPGRADE_UNKNOWN = "unknown"
DISTRO_UPGRADE_UNSTABLE = "unstable"
ERROR_ALL_PACKAGES_ALREADY_INSTALLED = "all-packages-already-installed"
ERROR_BAD_GPG_SIGNATURE = "bad-gpg-signature"
ERROR_CANCELLED_PRIORITY = "cancelled-priority"
ERROR_CANNOT_CANCEL = "cannot-cancel"
ERROR_CANNOT_DISABLE_REPOSITORY = "cannot-disable-repository"
ERROR_CANNOT_FETCH_SOURCES = "cannot-fetch-sources"
ERROR_CANNOT_GET_FILELIST = "cannot-get-filelist"
ERROR_CANNOT_GET_LOCK = "cannot-get-lock"
ERROR_CANNOT_GET_REQUIRES = "cannot-get-requires"
ERROR_CANNOT_INSTALL_REPO_UNSIGNED = "cannot-install-repo-unsigned"
ERROR_CANNOT_INSTALL_SOURCE_PACKAGE = "cannot-install-source-package"
ERROR_CANNOT_REMOVE_SYSTEM_PACKAGE = "cannot-remove-system-package"
ERROR_CANNOT_UPDATE_REPO_UNSIGNED = "cannot-update-repo-unsigned"
ERROR_CANNOT_WRITE_REPO_CONFIG = "cannot-write-repo-config"
ERROR_CREATE_THREAD_FAILED = "create-thread-failed"
ERROR_DEP_RESOLUTION_FAILED = "dep-resolution-failed"
ERROR_FAILED_CONFIG_PARSING = "failed-config-parsing"
ERROR_FAILED_FINALISE = "failed-finalise"
ERROR_FAILED_INITIALIZATION = "failed-initialization"
ERROR_FILE_CONFLICTS = "file-conflicts"
ERROR_FILE_NOT_FOUND = "file-not-found"
ERROR_FILTER_INVALID = "filter-invalid"
ERROR_GPG_FAILURE = "gpg-failure"
ERROR_GROUP_LIST_INVALID = "group-list-invalid"
ERROR_GROUP_NOT_FOUND = "group-not-found"
ERROR_INCOMPATIBLE_ARCHITECTURE = "incompatible-architecture"
ERROR_INSTALL_ROOT_INVALID = "install-root-invalid"
ERROR_INTERNAL_ERROR = "internal-error"
ERROR_INVALID_PACKAGE_FILE = "invalid-package-file"
ERROR_LOCAL_INSTALL_FAILED = "local-install-failed"
ERROR_LOCK_REQUIRED = "lock-required"
ERROR_MEDIA_CHANGE_REQUIRED = "media-change-required"
ERROR_MISSING_GPG_SIGNATURE = "missing-gpg-signature"
ERROR_NOT_AUTHORIZED = "not-authorized"
ERROR_NOT_SUPPORTED = "not-supported"
ERROR_NO_CACHE = "no-cache"
ERROR_NO_DISTRO_UPGRADE_DATA = "no-distro-upgrade-data"
ERROR_NO_LICENSE_AGREEMENT = "no-license-agreement"
ERROR_NO_MORE_MIRRORS_TO_TRY = "no-more-mirrors-to-try"
ERROR_NO_NETWORK = "no-network"
ERROR_NO_PACKAGES_TO_UPDATE = "no-packages-to-update"
ERROR_NO_SPACE_ON_DEVICE = "no-space-on-device"
ERROR_OOM = "out-of-memory"
ERROR_PACKAGE_ALREADY_INSTALLED = "package-already-installed"
ERROR_PACKAGE_CONFLICTS = "package-conflicts"
ERROR_PACKAGE_CORRUPT = "package-corrupt"
ERROR_PACKAGE_DATABASE_CHANGED = "package-database-changed"
ERROR_PACKAGE_DOWNLOAD_FAILED = "package-download-failed"
ERROR_PACKAGE_FAILED_TO_BUILD = "package-failed-to-build"
ERROR_PACKAGE_FAILED_TO_CONFIGURE = "package-failed-to-configure"
ERROR_PACKAGE_FAILED_TO_INSTALL = "package-failed-to-install"
ERROR_PACKAGE_FAILED_TO_REMOVE = "package-failed-to-remove"
ERROR_PACKAGE_ID_INVALID = "package-id-invalid"
ERROR_PACKAGE_INSTALL_BLOCKED = "package-install-blocked"
ERROR_PACKAGE_NOT_FOUND = "package-not-found"
ERROR_PACKAGE_NOT_INSTALLED = "package-not-installed"
ERROR_PROCESS_KILL = "process-kill"
ERROR_PROVIDE_TYPE_NOT_SUPPORTED = "provide-type-not-supported"
ERROR_REPO_ALREADY_SET = "repo-already-set"
ERROR_REPO_CONFIGURATION_ERROR = "repo-configuration-error"
ERROR_REPO_NOT_AVAILABLE = "repo-not-available"
ERROR_REPO_NOT_FOUND = "repo-not-found"
ERROR_RESTRICTED_DOWNLOAD = "restricted-download"
ERROR_TRANSACTION_CANCELLED = "transaction-cancelled"
ERROR_TRANSACTION_ERROR = "transaction-error"
ERROR_UNFINISHED_TRANSACTION = "unfinished-transaction"
ERROR_UNKNOWN = "unknown"
ERROR_UPDATE_FAILED_DUE_TO_RUNNING_PROCESS = "failed-due-to-running-process"
ERROR_UPDATE_NOT_FOUND = "update-not-found"
EXIT_CANCELLED = "cancelled"
EXIT_CANCELLED_PRIORITY = "cancelled-priority"
EXIT_EULA_REQUIRED = "eula-required"
EXIT_FAILED = "failed"
EXIT_KEY_REQUIRED = "key-required"
EXIT_KILLED = "killed"
EXIT_MEDIA_CHANGE_REQUIRED = "media-change-required"
EXIT_NEED_UNTRUSTED = "need-untrusted"
EXIT_REPAIR_REQUIRED = "repair-required"
EXIT_SKIP_TRANSACTION = "skip-transaction"
EXIT_SUCCESS = "success"
EXIT_UNKNOWN = "unknown"
FILTER_APPLICATION = "application"
FILTER_ARCH = "arch"
FILTER_BASENAME = "basename"
FILTER_COLLECTIONS = "collections"
FILTER_DEVELOPMENT = "devel"
FILTER_DOWNLOADED = "downloaded"
FILTER_FREE = "free"
FILTER_GUI = "gui"
FILTER_INSTALLED = "installed"
FILTER_NEWEST = "newest"
FILTER_NONE = "none"
FILTER_NOT_APPLICATION = "~application"
FILTER_NOT_ARCH = "~arch"
FILTER_NOT_BASENAME = "~basename"
FILTER_NOT_COLLECTIONS = "~collections"
FILTER_NOT_DEVELOPMENT = "~devel"
FILTER_NOT_DOWNLOADED = "~downloaded"
FILTER_NOT_FREE = "~free"
FILTER_NOT_GUI = "~gui"
FILTER_NOT_INSTALLED = "~installed"
FILTER_NOT_NEWEST = "~newest"
FILTER_NOT_SOURCE = "~source"
FILTER_NOT_SUPPORTED = "~supported"
FILTER_NOT_VISIBLE = "~visible"
FILTER_SOURCE = "source"
FILTER_SUPPORTED = "supported"
FILTER_UNKNOWN = "unknown"
FILTER_VISIBLE = "visible"
GROUP_ACCESSIBILITY = "accessibility"
GROUP_ACCESSORIES = "accessories"
GROUP_ADMIN_TOOLS = "admin-tools"
GROUP_COLLECTIONS = "collections"
GROUP_COMMUNICATION = "communication"
GROUP_DESKTOP_GNOME = "desktop-gnome"
GROUP_DESKTOP_KDE = "desktop-kde"
GROUP_DESKTOP_OTHER = "desktop-other"
GROUP_DESKTOP_XFCE = "desktop-xfce"
GROUP_DOCUMENTATION = "documentation"
GROUP_EDUCATION = "education"
GROUP_ELECTRONICS = "electronics"
GROUP_FONTS = "fonts"
GROUP_GAMES = "games"
GROUP_GRAPHICS = "graphics"
GROUP_INTERNET = "internet"
GROUP_LEGACY = "legacy"
GROUP_LOCALIZATION = "localization"
GROUP_MAPS = "maps"
GROUP_MULTIMEDIA = "multimedia"
GROUP_NETWORK = "network"
GROUP_NEWEST = "newest"
GROUP_OFFICE = "office"
GROUP_OTHER = "other"
GROUP_POWER_MANAGEMENT = "power-management"
GROUP_PROGRAMMING = "programming"
GROUP_PUBLISHING = "publishing"
GROUP_REPOS = "repos"
GROUP_SCIENCE = "science"
GROUP_SECURITY = "security"
GROUP_SERVERS = "servers"
GROUP_SYSTEM = "system"
GROUP_UNKNOWN = "unknown"
GROUP_VENDOR = "vendor"
GROUP_VIRTUALIZATION = "virtualization"
INFO_AVAILABLE = "available"
INFO_BLOCKED = "blocked"
INFO_BUGFIX = "bugfix"
INFO_CLEANUP = "cleanup"
INFO_COLLECTION_AVAILABLE = "collection-available"
INFO_COLLECTION_INSTALLED = "collection-installed"
INFO_DECOMPRESSING = "decompressing"
INFO_DOWNGRADING = "downgrading"
INFO_DOWNLOADING = "downloading"
INFO_ENHANCEMENT = "enhancement"
INFO_FINISHED = "finished"
INFO_IMPORTANT = "important"
INFO_INSTALLED = "installed"
INFO_INSTALLING = "installing"
INFO_LOW = "low"
INFO_NORMAL = "normal"
INFO_OBSOLETING = "obsoleting"
INFO_PREPARING = "preparing"
INFO_REINSTALLING = "reinstalling"
INFO_REMOVING = "removing"
INFO_SECURITY = "security"
INFO_TRUSTED = "trusted"
INFO_UNAVAILABLE = "unavailable"
INFO_UNKNOWN = "unknown"
INFO_UNTRUSTED = "untrusted"
INFO_UPDATING = "updating"
MEDIA_TYPE_CD = "cd"
MEDIA_TYPE_DISC = "disc"
MEDIA_TYPE_DVD = "dvd"
MEDIA_TYPE_UNKNOWN = "unknown"
NETWORK_MOBILE = "mobile"
NETWORK_OFFLINE = "offline"
NETWORK_ONLINE = "online"
NETWORK_UNKNOWN = "unknown"
NETWORK_WIFI = "wifi"
NETWORK_WIRED = "wired"
RESTART_APPLICATION = "application"
RESTART_NONE = "none"
RESTART_SECURITY_SESSION = "security-session"
RESTART_SECURITY_SYSTEM = "security-system"
RESTART_SESSION = "session"
RESTART_SYSTEM = "system"
RESTART_UNKNOWN = "unknown"
ROLE_ACCEPT_EULA = "accept-eula"
ROLE_CANCEL = "cancel"
ROLE_DEPENDS_ON = "depends-on"
ROLE_DOWNLOAD_PACKAGES = "download-packages"
ROLE_GET_CATEGORIES = "get-categories"
ROLE_GET_DETAILS = "get-details"
ROLE_GET_DETAILS_LOCAL = "get-details-local"
ROLE_GET_DISTRO_UPGRADES = "get-distro-upgrades"
ROLE_GET_FILES = "get-files"
ROLE_GET_FILES_LOCAL = "get-files-local"
ROLE_GET_OLD_TRANSACTIONS = "get-old-transactions"
ROLE_GET_PACKAGES = "get-packages"
ROLE_GET_REPO_LIST = "get-repo-list"
ROLE_GET_UPDATES = "get-updates"
ROLE_GET_UPDATE_DETAIL = "get-update-detail"
ROLE_INSTALL_FILES = "install-files"
ROLE_INSTALL_PACKAGES = "install-packages"
ROLE_INSTALL_SIGNATURE = "install-signature"
ROLE_REFRESH_CACHE = "refresh-cache"
ROLE_REMOVE_PACKAGES = "remove-packages"
ROLE_REPAIR_SYSTEM = "repair-system"
ROLE_REPO_ENABLE = "repo-enable"
ROLE_REPO_REMOVE = "repo-remove"
ROLE_REPO_SET_DATA = "repo-set-data"
ROLE_REQUIRED_BY = "required-by"
ROLE_RESOLVE = "resolve"
ROLE_SEARCH_DETAILS = "search-details"
ROLE_SEARCH_FILE = "search-file"
ROLE_SEARCH_GROUP = "search-group"
ROLE_SEARCH_NAME = "search-name"
ROLE_UNKNOWN = "unknown"
ROLE_UPDATE_PACKAGES = "update-packages"
ROLE_UPGRADE_SYSTEM = "upgrade-system"
ROLE_WHAT_PROVIDES = "what-provides"
SIGTYPE_GPG = "gpg"
SIGTYPE_UNKNOWN = "unknown"
STATUS_CANCEL = "cancel"
STATUS_CHECK_EXECUTABLE_FILES = "check-executable-files"
STATUS_CHECK_LIBRARIES = "check-libraries"
STATUS_CLEANUP = "cleanup"
STATUS_COMMIT = "commit"
STATUS_COPY_FILES = "copy-files"
STATUS_DEP_RESOLVE = "dep-resolve"
STATUS_DOWNLOAD = "download"
STATUS_DOWNLOAD_CHANGELOG = "download-changelog"
STATUS_DOWNLOAD_FILELIST = "download-filelist"
STATUS_DOWNLOAD_GROUP = "download-group"
STATUS_DOWNLOAD_PACKAGELIST = "download-packagelist"
STATUS_DOWNLOAD_REPOSITORY = "download-repository"
STATUS_DOWNLOAD_UPDATEINFO = "download-updateinfo"
STATUS_FINISHED = "finished"
STATUS_GENERATE_PACKAGE_LIST = "generate-package-list"
STATUS_INFO = "info"
STATUS_INSTALL = "install"
STATUS_LOADING_CACHE = "loading-cache"
STATUS_OBSOLETE = "obsolete"
STATUS_QUERY = "query"
STATUS_REFRESH_CACHE = "refresh-cache"
STATUS_REMOVE = "remove"
STATUS_REPACKAGING = "repackaging"
STATUS_REQUEST = "request"
STATUS_RUNNING = "running"
STATUS_RUN_HOOK = "run-hook"
STATUS_SCAN_APPLICATIONS = "scan-applications"
STATUS_SCAN_PROCESS_LIST = "scan-process-list"
STATUS_SETUP = "setup"
STATUS_SIG_CHECK = "sig-check"
STATUS_TEST_COMMIT = "test-commit"
STATUS_UNKNOWN = "unknown"
STATUS_UPDATE = "update"
STATUS_WAIT = "wait"
STATUS_WAITING_FOR_AUTH = "waiting-for-auth"
STATUS_WAITING_FOR_LOCK = "waiting-for-lock"
TRANSACTION_FLAG_ALLOW_DOWNGRADE = "allow-downgrade"
TRANSACTION_FLAG_ALLOW_REINSTALL = "allow-reinstall"
TRANSACTION_FLAG_JUST_REINSTALL = "just-reinstall"
TRANSACTION_FLAG_NONE = "none"
TRANSACTION_FLAG_ONLY_DOWNLOAD = "only-download"
TRANSACTION_FLAG_ONLY_TRUSTED = "only-trusted"
TRANSACTION_FLAG_SIMULATE = "simulate"
UPDATE_STATE_STABLE = "stable"
UPDATE_STATE_TESTING = "testing"
UPDATE_STATE_UNKNOWN = "unknown"
UPDATE_STATE_UNSTABLE = "unstable"
UPGRADE_KIND_COMPLETE = "complete"
UPGRADE_KIND_DEFAULT = "default"
UPGRADE_KIND_MINIMAL = "minimal"
UPGRADE_KIND_UNKNOWN = "unknown"
