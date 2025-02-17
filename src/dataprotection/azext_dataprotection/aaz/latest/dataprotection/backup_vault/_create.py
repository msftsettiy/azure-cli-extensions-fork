# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "dataprotection backup-vault create",
    is_experimental=True,
)
class Create(AAZCommand):
    """Create a BackupVault resource belonging to a resource group.

    :example: Create BackupVault
        az dataprotection backup-vault create --type "None" --location "WestUS" --azure-monitor-alerts-for-job-failures "Enabled" --storage-setting "[{type:'LocallyRedundant',datastore-type:'VaultStore'}]" --tags key1="val1" --resource-group "SampleResourceGroup" --vault-name "swaggerExample"

    :example: Create BackupVault With MSI
        az dataprotection backup-vault create --type "systemAssigned" --location "WestUS" --azure-monitor-alerts-for-job-failures "Enabled" --storage-setting "[{type:'LocallyRedundant',datastore-type:'VaultStore'}]" --tags key1="val1" --resource-group "SampleResourceGroup" --vault-name "swaggerExample"
    """

    _aaz_info = {
        "version": "2022-12-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.dataprotection/backupvaults/{}", "2022-12-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.vault_name = AAZStrArg(
            options=["--vault-name"],
            help="The name of the backup vault.",
            required=True,
        )

        # define Arg Group "Identity"

        _args_schema = cls._args_schema
        _args_schema.type = AAZStrArg(
            options=["--type"],
            arg_group="Identity",
            help="The identityType which can be either SystemAssigned or None",
        )

        # define Arg Group "Monitoring Settings Azure Monitor Alert Settings"

        _args_schema = cls._args_schema
        _args_schema.azure_monitor_alerts_for_job_failures = AAZStrArg(
            options=["--job-failure-alerts", "--azure-monitor-alerts-for-job-failures"],
            arg_group="Monitoring Settings Azure Monitor Alert Settings",
            help="Property that specifies whether built-in Azure Monitor alerts should be fired for all failed jobs.",
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.e_tag = AAZStrArg(
            options=["--e-tag"],
            arg_group="Parameters",
            help="Optional ETag.",
        )
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Parameters",
            help="Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Space-separated tags: key[=value] [key[=value] ...]. Use \"\" to clear existing tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.storage_setting = AAZListArg(
            options=["--storage-setting"],
            singular_options=["--storage-settings"],
            arg_group="Properties",
            help={"short-summary": "Storage Settings. Usage: --storage-setting \"[{type:'LocallyRedundant',datastore-type:'VaultStore'}]\"", "long-summary": "Multiple actions can be specified by using more than one --storage-setting argument.\nThe \"--storage-settings\" parameter exists for backwards compatibility. The updated command is --storage-setting.\nUsage for --storage-settings: --storage-settings type=XX datastore-type=XX."},
            required=True,
        )

        storage_setting = cls._args_schema.storage_setting
        storage_setting.Element = AAZObjectArg()

        _element = cls._args_schema.storage_setting.Element
        _element.datastore_type = AAZStrArg(
            options=["datastore-type"],
            help="Gets or sets the type of the datastore.",
            enum={"ArchiveStore": "ArchiveStore", "OperationalStore": "OperationalStore", "VaultStore": "VaultStore"},
        )
        _element.type = AAZStrArg(
            options=["type"],
            help="Gets or sets the type.",
            enum={"GeoRedundant": "GeoRedundant", "LocallyRedundant": "LocallyRedundant", "ZoneRedundant": "ZoneRedundant"},
        )

        # define Arg Group "SecuritySettings"

        _args_schema = cls._args_schema
        _args_schema.immutability_state = AAZStrArg(
            options=["--immutability-state"],
            arg_group="SecuritySettings",
            help={"short-summary": "Immutability state", "long-summary": "Use this parameter to configure immutability settings for the vault. Allowed values are Disabled, Unlocked and Locked. By default, immutability is \"Disabled\" for the vault. \"Unlocked\" means that immutability is enabled for the vault and can be reversed. \"Locked\" means that immutability is enabled for the vault and cannot be reversed."},
            enum={"Disabled": "Disabled", "Locked": "Locked", "Unlocked": "Unlocked"},
        )

        # define Arg Group "SoftDeleteSettings"

        _args_schema = cls._args_schema
        _args_schema.retention_duration_in_days = AAZFloatArg(
            options=["--soft-delete-retention", "--retention-duration-in-days"],
            arg_group="SoftDeleteSettings",
            help="Soft delete retention duration",
        )
        _args_schema.soft_delete_state = AAZStrArg(
            options=["--soft-delete-state"],
            arg_group="SoftDeleteSettings",
            help="State of soft delete",
            enum={"AlwaysOn": "AlwaysOn", "Off": "Off", "On": "On"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.BackupVaultsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class BackupVaultsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataProtection/backupVaults/{vaultName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "vaultName", self.ctx.args.vault_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-12-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("eTag", AAZStrType, ".e_tag")
            _builder.set_prop("identity", AAZObjectType)
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            identity = _builder.get(".identity")
            if identity is not None:
                identity.set_prop("type", AAZStrType, ".type")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("monitoringSettings", AAZObjectType)
                properties.set_prop("securitySettings", AAZObjectType)
                properties.set_prop("storageSettings", AAZListType, ".storage_setting", typ_kwargs={"flags": {"required": True}})

            monitoring_settings = _builder.get(".properties.monitoringSettings")
            if monitoring_settings is not None:
                monitoring_settings.set_prop("azureMonitorAlertSettings", AAZObjectType)

            azure_monitor_alert_settings = _builder.get(".properties.monitoringSettings.azureMonitorAlertSettings")
            if azure_monitor_alert_settings is not None:
                azure_monitor_alert_settings.set_prop("alertsForAllJobFailures", AAZStrType, ".azure_monitor_alerts_for_job_failures")

            security_settings = _builder.get(".properties.securitySettings")
            if security_settings is not None:
                security_settings.set_prop("immutabilitySettings", AAZObjectType)
                security_settings.set_prop("softDeleteSettings", AAZObjectType)

            immutability_settings = _builder.get(".properties.securitySettings.immutabilitySettings")
            if immutability_settings is not None:
                immutability_settings.set_prop("state", AAZStrType, ".immutability_state")

            soft_delete_settings = _builder.get(".properties.securitySettings.softDeleteSettings")
            if soft_delete_settings is not None:
                soft_delete_settings.set_prop("retentionDurationInDays", AAZFloatType, ".retention_duration_in_days")
                soft_delete_settings.set_prop("state", AAZStrType, ".soft_delete_state")

            storage_settings = _builder.get(".properties.storageSettings")
            if storage_settings is not None:
                storage_settings.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.storageSettings[]")
            if _elements is not None:
                _elements.set_prop("datastoreType", AAZStrType, ".datastore_type")
                _elements.set_prop("type", AAZStrType, ".type")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.e_tag = AAZStrType(
                serialized_name="eTag",
            )
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.identity = AAZObjectType()
            _schema_on_200_201.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"required": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200_201.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType()

            properties = cls._schema_on_200_201.properties
            properties.feature_settings = AAZObjectType(
                serialized_name="featureSettings",
            )
            properties.is_vault_protected_by_resource_guard = AAZBoolType(
                serialized_name="isVaultProtectedByResourceGuard",
                flags={"read_only": True},
            )
            properties.monitoring_settings = AAZObjectType(
                serialized_name="monitoringSettings",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.resource_move_details = AAZObjectType(
                serialized_name="resourceMoveDetails",
            )
            properties.resource_move_state = AAZStrType(
                serialized_name="resourceMoveState",
                flags={"read_only": True},
            )
            properties.security_settings = AAZObjectType(
                serialized_name="securitySettings",
            )
            properties.storage_settings = AAZListType(
                serialized_name="storageSettings",
                flags={"required": True},
            )

            feature_settings = cls._schema_on_200_201.properties.feature_settings
            feature_settings.cross_subscription_restore_settings = AAZObjectType(
                serialized_name="crossSubscriptionRestoreSettings",
            )

            cross_subscription_restore_settings = cls._schema_on_200_201.properties.feature_settings.cross_subscription_restore_settings
            cross_subscription_restore_settings.state = AAZStrType()

            monitoring_settings = cls._schema_on_200_201.properties.monitoring_settings
            monitoring_settings.azure_monitor_alert_settings = AAZObjectType(
                serialized_name="azureMonitorAlertSettings",
            )

            azure_monitor_alert_settings = cls._schema_on_200_201.properties.monitoring_settings.azure_monitor_alert_settings
            azure_monitor_alert_settings.alerts_for_all_job_failures = AAZStrType(
                serialized_name="alertsForAllJobFailures",
            )

            resource_move_details = cls._schema_on_200_201.properties.resource_move_details
            resource_move_details.completion_time_utc = AAZStrType(
                serialized_name="completionTimeUtc",
            )
            resource_move_details.operation_id = AAZStrType(
                serialized_name="operationId",
            )
            resource_move_details.source_resource_path = AAZStrType(
                serialized_name="sourceResourcePath",
            )
            resource_move_details.start_time_utc = AAZStrType(
                serialized_name="startTimeUtc",
            )
            resource_move_details.target_resource_path = AAZStrType(
                serialized_name="targetResourcePath",
            )

            security_settings = cls._schema_on_200_201.properties.security_settings
            security_settings.immutability_settings = AAZObjectType(
                serialized_name="immutabilitySettings",
            )
            security_settings.soft_delete_settings = AAZObjectType(
                serialized_name="softDeleteSettings",
            )

            immutability_settings = cls._schema_on_200_201.properties.security_settings.immutability_settings
            immutability_settings.state = AAZStrType()

            soft_delete_settings = cls._schema_on_200_201.properties.security_settings.soft_delete_settings
            soft_delete_settings.retention_duration_in_days = AAZFloatType(
                serialized_name="retentionDurationInDays",
            )
            soft_delete_settings.state = AAZStrType()

            storage_settings = cls._schema_on_200_201.properties.storage_settings
            storage_settings.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.storage_settings.Element
            _element.datastore_type = AAZStrType(
                serialized_name="datastoreType",
            )
            _element.type = AAZStrType()

            system_data = cls._schema_on_200_201.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
