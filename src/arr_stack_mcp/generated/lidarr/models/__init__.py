"""Contains all the data models used in inputs/outputs"""

from .add_album_options import AddAlbumOptions
from .add_artist_options import AddArtistOptions
from .album_add_type import AlbumAddType
from .album_release_resource import AlbumReleaseResource
from .album_resource import AlbumResource
from .album_resource_paging_resource import AlbumResourcePagingResource
from .album_statistics_resource import AlbumStatisticsResource
from .album_studio_artist_resource import AlbumStudioArtistResource
from .album_studio_resource import AlbumStudioResource
from .albums_monitored_resource import AlbumsMonitoredResource
from .allow_fingerprinting import AllowFingerprinting
from .apply_tags import ApplyTags
from .artist_editor_resource import ArtistEditorResource
from .artist_resource import ArtistResource
from .artist_statistics_resource import ArtistStatisticsResource
from .artist_status_type import ArtistStatusType
from .artist_title_info import ArtistTitleInfo
from .authentication_required_type import AuthenticationRequiredType
from .authentication_type import AuthenticationType
from .auto_tagging_resource import AutoTaggingResource
from .auto_tagging_specification_schema import AutoTaggingSpecificationSchema
from .backup_resource import BackupResource
from .backup_type import BackupType
from .blocklist_bulk_resource import BlocklistBulkResource
from .blocklist_resource import BlocklistResource
from .blocklist_resource_paging_resource import BlocklistResourcePagingResource
from .certificate_validation_type import CertificateValidationType
from .command import Command
from .command_priority import CommandPriority
from .command_resource import CommandResource
from .command_result import CommandResult
from .command_status import CommandStatus
from .command_trigger import CommandTrigger
from .custom_filter_resource import CustomFilterResource
from .custom_filter_resource_filters_type_0_item import (
    CustomFilterResourceFiltersType0Item,
)
from .custom_format_bulk_resource import CustomFormatBulkResource
from .custom_format_resource import CustomFormatResource
from .custom_format_specification_schema import CustomFormatSpecificationSchema
from .database_type import DatabaseType
from .delay_profile_resource import DelayProfileResource
from .disk_space_resource import DiskSpaceResource
from .download_client_bulk_resource import DownloadClientBulkResource
from .download_client_config_resource import DownloadClientConfigResource
from .download_client_resource import DownloadClientResource
from .download_protocol import DownloadProtocol
from .entity_history_event_type import EntityHistoryEventType
from .field import Field
from .file_date_type import FileDateType
from .health_check_result import HealthCheckResult
from .health_resource import HealthResource
from .history_resource import HistoryResource
from .history_resource_data_type_0 import HistoryResourceDataType0
from .history_resource_paging_resource import HistoryResourcePagingResource
from .host_config_resource import HostConfigResource
from .import_list_bulk_resource import ImportListBulkResource
from .import_list_exclusion_resource import ImportListExclusionResource
from .import_list_monitor_type import ImportListMonitorType
from .import_list_resource import ImportListResource
from .import_list_type import ImportListType
from .indexer_bulk_resource import IndexerBulkResource
from .indexer_config_resource import IndexerConfigResource
from .indexer_flag_resource import IndexerFlagResource
from .indexer_resource import IndexerResource
from .iso_country import IsoCountry
from .language_resource import LanguageResource
from .links import Links
from .localization_resource import LocalizationResource
from .localization_resource_strings_type_0 import LocalizationResourceStringsType0
from .log_file_resource import LogFileResource
from .log_resource import LogResource
from .log_resource_paging_resource import LogResourcePagingResource
from .manual_import_resource import ManualImportResource
from .manual_import_update_resource import ManualImportUpdateResource
from .media_cover import MediaCover
from .media_cover_types import MediaCoverTypes
from .media_info_model import MediaInfoModel
from .media_info_resource import MediaInfoResource
from .media_management_config_resource import MediaManagementConfigResource
from .medium_resource import MediumResource
from .member import Member
from .metadata_profile_resource import MetadataProfileResource
from .metadata_provider_config_resource import MetadataProviderConfigResource
from .metadata_resource import MetadataResource
from .monitor_types import MonitorTypes
from .monitoring_options import MonitoringOptions
from .naming_config_resource import NamingConfigResource
from .new_item_monitor_types import NewItemMonitorTypes
from .notification_resource import NotificationResource
from .parse_resource import ParseResource
from .parsed_album_info import ParsedAlbumInfo
from .parsed_track_info import ParsedTrackInfo
from .ping_resource import PingResource
from .post_login_body import PostLoginBody
from .primary_album_type import PrimaryAlbumType
from .privacy_level import PrivacyLevel
from .profile_format_item_resource import ProfileFormatItemResource
from .profile_primary_album_type_item_resource import (
    ProfilePrimaryAlbumTypeItemResource,
)
from .profile_release_status_item_resource import ProfileReleaseStatusItemResource
from .profile_secondary_album_type_item_resource import (
    ProfileSecondaryAlbumTypeItemResource,
)
from .proper_download_types import ProperDownloadTypes
from .provider_message import ProviderMessage
from .provider_message_type import ProviderMessageType
from .proxy_type import ProxyType
from .quality import Quality
from .quality_definition_resource import QualityDefinitionResource
from .quality_model import QualityModel
from .quality_profile_quality_item_resource import QualityProfileQualityItemResource
from .quality_profile_resource import QualityProfileResource
from .queue_bulk_resource import QueueBulkResource
from .queue_resource import QueueResource
from .queue_resource_paging_resource import QueueResourcePagingResource
from .queue_status_resource import QueueStatusResource
from .ratings import Ratings
from .rejection import Rejection
from .rejection_type import RejectionType
from .release_profile_resource import ReleaseProfileResource
from .release_resource import ReleaseResource
from .release_status import ReleaseStatus
from .remote_path_mapping_resource import RemotePathMappingResource
from .rename_track_resource import RenameTrackResource
from .rescan_after_refresh_type import RescanAfterRefreshType
from .retag_track_resource import RetagTrackResource
from .revision import Revision
from .root_folder_resource import RootFolderResource
from .runtime_mode import RuntimeMode
from .search_resource import SearchResource
from .secondary_album_type import SecondaryAlbumType
from .select_option import SelectOption
from .sort_direction import SortDirection
from .system_resource import SystemResource
from .tag_details_resource import TagDetailsResource
from .tag_difference import TagDifference
from .tag_resource import TagResource
from .task_resource import TaskResource
from .track_file_list_resource import TrackFileListResource
from .track_file_resource import TrackFileResource
from .track_resource import TrackResource
from .tracked_download_state import TrackedDownloadState
from .tracked_download_status import TrackedDownloadStatus
from .tracked_download_status_message import TrackedDownloadStatusMessage
from .ui_config_resource import UiConfigResource
from .update_changes import UpdateChanges
from .update_mechanism import UpdateMechanism
from .update_resource import UpdateResource
from .write_audio_tags_type import WriteAudioTagsType

__all__ = (
    "AddAlbumOptions",
    "AddArtistOptions",
    "AlbumAddType",
    "AlbumReleaseResource",
    "AlbumResource",
    "AlbumResourcePagingResource",
    "AlbumsMonitoredResource",
    "AlbumStatisticsResource",
    "AlbumStudioArtistResource",
    "AlbumStudioResource",
    "AllowFingerprinting",
    "ApplyTags",
    "ArtistEditorResource",
    "ArtistResource",
    "ArtistStatisticsResource",
    "ArtistStatusType",
    "ArtistTitleInfo",
    "AuthenticationRequiredType",
    "AuthenticationType",
    "AutoTaggingResource",
    "AutoTaggingSpecificationSchema",
    "BackupResource",
    "BackupType",
    "BlocklistBulkResource",
    "BlocklistResource",
    "BlocklistResourcePagingResource",
    "CertificateValidationType",
    "Command",
    "CommandPriority",
    "CommandResource",
    "CommandResult",
    "CommandStatus",
    "CommandTrigger",
    "CustomFilterResource",
    "CustomFilterResourceFiltersType0Item",
    "CustomFormatBulkResource",
    "CustomFormatResource",
    "CustomFormatSpecificationSchema",
    "DatabaseType",
    "DelayProfileResource",
    "DiskSpaceResource",
    "DownloadClientBulkResource",
    "DownloadClientConfigResource",
    "DownloadClientResource",
    "DownloadProtocol",
    "EntityHistoryEventType",
    "Field",
    "FileDateType",
    "HealthCheckResult",
    "HealthResource",
    "HistoryResource",
    "HistoryResourceDataType0",
    "HistoryResourcePagingResource",
    "HostConfigResource",
    "ImportListBulkResource",
    "ImportListExclusionResource",
    "ImportListMonitorType",
    "ImportListResource",
    "ImportListType",
    "IndexerBulkResource",
    "IndexerConfigResource",
    "IndexerFlagResource",
    "IndexerResource",
    "IsoCountry",
    "LanguageResource",
    "Links",
    "LocalizationResource",
    "LocalizationResourceStringsType0",
    "LogFileResource",
    "LogResource",
    "LogResourcePagingResource",
    "ManualImportResource",
    "ManualImportUpdateResource",
    "MediaCover",
    "MediaCoverTypes",
    "MediaInfoModel",
    "MediaInfoResource",
    "MediaManagementConfigResource",
    "MediumResource",
    "Member",
    "MetadataProfileResource",
    "MetadataProviderConfigResource",
    "MetadataResource",
    "MonitoringOptions",
    "MonitorTypes",
    "NamingConfigResource",
    "NewItemMonitorTypes",
    "NotificationResource",
    "ParsedAlbumInfo",
    "ParsedTrackInfo",
    "ParseResource",
    "PingResource",
    "PostLoginBody",
    "PrimaryAlbumType",
    "PrivacyLevel",
    "ProfileFormatItemResource",
    "ProfilePrimaryAlbumTypeItemResource",
    "ProfileReleaseStatusItemResource",
    "ProfileSecondaryAlbumTypeItemResource",
    "ProperDownloadTypes",
    "ProviderMessage",
    "ProviderMessageType",
    "ProxyType",
    "Quality",
    "QualityDefinitionResource",
    "QualityModel",
    "QualityProfileQualityItemResource",
    "QualityProfileResource",
    "QueueBulkResource",
    "QueueResource",
    "QueueResourcePagingResource",
    "QueueStatusResource",
    "Ratings",
    "Rejection",
    "RejectionType",
    "ReleaseProfileResource",
    "ReleaseResource",
    "ReleaseStatus",
    "RemotePathMappingResource",
    "RenameTrackResource",
    "RescanAfterRefreshType",
    "RetagTrackResource",
    "Revision",
    "RootFolderResource",
    "RuntimeMode",
    "SearchResource",
    "SecondaryAlbumType",
    "SelectOption",
    "SortDirection",
    "SystemResource",
    "TagDetailsResource",
    "TagDifference",
    "TagResource",
    "TaskResource",
    "TrackedDownloadState",
    "TrackedDownloadStatus",
    "TrackedDownloadStatusMessage",
    "TrackFileListResource",
    "TrackFileResource",
    "TrackResource",
    "UiConfigResource",
    "UpdateChanges",
    "UpdateMechanism",
    "UpdateResource",
    "WriteAudioTagsType",
)
