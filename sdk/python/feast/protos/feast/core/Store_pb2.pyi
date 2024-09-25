"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file

* Copyright 2019 The Feast Authors
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*     https://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Store(google.protobuf.message.Message):
    """Store provides a location where Feast reads and writes feature values.
    Feature values will be written to the Store in the form of FeatureRow elements.
    The way FeatureRow is encoded and decoded when it is written to and read from
    the Store depends on the type of the Store.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _StoreType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StoreTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Store._StoreType.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        INVALID: Store._StoreType.ValueType  # 0
        REDIS: Store._StoreType.ValueType  # 1
        """Redis stores a FeatureRow element as a key, value pair.

        The Redis data types used (https://redis.io/topics/data-types):
        - key: STRING
        - value: STRING

        Encodings:
        - key: byte array of RedisKey (refer to feast.storage.RedisKeyV2)
        - value: Redis hashmap
        """
        REDIS_CLUSTER: Store._StoreType.ValueType  # 4

    class StoreType(_StoreType, metaclass=_StoreTypeEnumTypeWrapper): ...
    INVALID: Store.StoreType.ValueType  # 0
    REDIS: Store.StoreType.ValueType  # 1
    """Redis stores a FeatureRow element as a key, value pair.

    The Redis data types used (https://redis.io/topics/data-types):
    - key: STRING
    - value: STRING

    Encodings:
    - key: byte array of RedisKey (refer to feast.storage.RedisKeyV2)
    - value: Redis hashmap
    """
    REDIS_CLUSTER: Store.StoreType.ValueType  # 4

    class RedisConfig(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        HOST_FIELD_NUMBER: builtins.int
        PORT_FIELD_NUMBER: builtins.int
        INITIAL_BACKOFF_MS_FIELD_NUMBER: builtins.int
        MAX_RETRIES_FIELD_NUMBER: builtins.int
        FLUSH_FREQUENCY_SECONDS_FIELD_NUMBER: builtins.int
        SSL_FIELD_NUMBER: builtins.int
        host: builtins.str
        port: builtins.int
        initial_backoff_ms: builtins.int
        """Optional. The number of milliseconds to wait before retrying failed Redis connection.
        By default, Feast uses exponential backoff policy and "initial_backoff_ms" sets the initial wait duration.
        """
        max_retries: builtins.int
        """Optional. Maximum total number of retries for connecting to Redis. Default to zero retries."""
        flush_frequency_seconds: builtins.int
        """Optional. How often flush data to redis"""
        ssl: builtins.bool
        """Optional. Connect over SSL."""
        def __init__(
            self,
            *,
            host: builtins.str = ...,
            port: builtins.int = ...,
            initial_backoff_ms: builtins.int = ...,
            max_retries: builtins.int = ...,
            flush_frequency_seconds: builtins.int = ...,
            ssl: builtins.bool = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["flush_frequency_seconds", b"flush_frequency_seconds", "host", b"host", "initial_backoff_ms", b"initial_backoff_ms", "max_retries", b"max_retries", "port", b"port", "ssl", b"ssl"]) -> None: ...

    class RedisClusterConfig(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class _ReadFrom:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _ReadFromEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Store.RedisClusterConfig._ReadFrom.ValueType], builtins.type):  # noqa: F821
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            MASTER: Store.RedisClusterConfig._ReadFrom.ValueType  # 0
            MASTER_PREFERRED: Store.RedisClusterConfig._ReadFrom.ValueType  # 1
            REPLICA: Store.RedisClusterConfig._ReadFrom.ValueType  # 2
            REPLICA_PREFERRED: Store.RedisClusterConfig._ReadFrom.ValueType  # 3

        class ReadFrom(_ReadFrom, metaclass=_ReadFromEnumTypeWrapper):
            """Optional. Priority of nodes when reading from cluster"""

        MASTER: Store.RedisClusterConfig.ReadFrom.ValueType  # 0
        MASTER_PREFERRED: Store.RedisClusterConfig.ReadFrom.ValueType  # 1
        REPLICA: Store.RedisClusterConfig.ReadFrom.ValueType  # 2
        REPLICA_PREFERRED: Store.RedisClusterConfig.ReadFrom.ValueType  # 3

        CONNECTION_STRING_FIELD_NUMBER: builtins.int
        INITIAL_BACKOFF_MS_FIELD_NUMBER: builtins.int
        MAX_RETRIES_FIELD_NUMBER: builtins.int
        FLUSH_FREQUENCY_SECONDS_FIELD_NUMBER: builtins.int
        KEY_PREFIX_FIELD_NUMBER: builtins.int
        ENABLE_FALLBACK_FIELD_NUMBER: builtins.int
        FALLBACK_PREFIX_FIELD_NUMBER: builtins.int
        READ_FROM_FIELD_NUMBER: builtins.int
        connection_string: builtins.str
        """List of Redis Uri for all the nodes in Redis Cluster, comma separated. Eg. host1:6379, host2:6379"""
        initial_backoff_ms: builtins.int
        max_retries: builtins.int
        flush_frequency_seconds: builtins.int
        """Optional. How often flush data to redis"""
        key_prefix: builtins.str
        """Optional. Append a prefix to the Redis Key"""
        enable_fallback: builtins.bool
        """Optional. Enable fallback to another key prefix if the original key is not present.
        Useful for migrating key prefix without re-ingestion. Disabled by default.
        """
        fallback_prefix: builtins.str
        """Optional. This would be the fallback prefix to use if enable_fallback is true."""
        read_from: global___Store.RedisClusterConfig.ReadFrom.ValueType
        def __init__(
            self,
            *,
            connection_string: builtins.str = ...,
            initial_backoff_ms: builtins.int = ...,
            max_retries: builtins.int = ...,
            flush_frequency_seconds: builtins.int = ...,
            key_prefix: builtins.str = ...,
            enable_fallback: builtins.bool = ...,
            fallback_prefix: builtins.str = ...,
            read_from: global___Store.RedisClusterConfig.ReadFrom.ValueType = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["connection_string", b"connection_string", "enable_fallback", b"enable_fallback", "fallback_prefix", b"fallback_prefix", "flush_frequency_seconds", b"flush_frequency_seconds", "initial_backoff_ms", b"initial_backoff_ms", "key_prefix", b"key_prefix", "max_retries", b"max_retries", "read_from", b"read_from"]) -> None: ...

    class Subscription(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        PROJECT_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        EXCLUDE_FIELD_NUMBER: builtins.int
        project: builtins.str
        """Name of project that the feature sets belongs to. This can be one of
        - [project_name]
        - *
        If an asterisk is provided, filtering on projects will be disabled. All projects will
        be matched. It is NOT possible to provide an asterisk with a string in order to do
        pattern matching.
        """
        name: builtins.str
        """Name of the desired feature set. Asterisks can be used as wildcards in the name.
        Matching on names is only permitted if a specific project is defined. It is disallowed
        If the project name is set to "*"
        e.g.
        - * can be used to match all feature sets
        - my-feature-set* can be used to match all features prefixed by "my-feature-set"
        - my-feature-set-6 can be used to select a single feature set
        """
        exclude: builtins.bool
        """All matches with exclude enabled will be filtered out instead of added"""
        def __init__(
            self,
            *,
            project: builtins.str = ...,
            name: builtins.str = ...,
            exclude: builtins.bool = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["exclude", b"exclude", "name", b"name", "project", b"project"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    SUBSCRIPTIONS_FIELD_NUMBER: builtins.int
    REDIS_CONFIG_FIELD_NUMBER: builtins.int
    REDIS_CLUSTER_CONFIG_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the store."""
    type: global___Store.StoreType.ValueType
    """Type of store."""
    @property
    def subscriptions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Store.Subscription]:
        """Feature sets to subscribe to."""
    @property
    def redis_config(self) -> global___Store.RedisConfig: ...
    @property
    def redis_cluster_config(self) -> global___Store.RedisClusterConfig: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        type: global___Store.StoreType.ValueType = ...,
        subscriptions: collections.abc.Iterable[global___Store.Subscription] | None = ...,
        redis_config: global___Store.RedisConfig | None = ...,
        redis_cluster_config: global___Store.RedisClusterConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config", b"config", "redis_cluster_config", b"redis_cluster_config", "redis_config", b"redis_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config", b"config", "name", b"name", "redis_cluster_config", b"redis_cluster_config", "redis_config", b"redis_config", "subscriptions", b"subscriptions", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["config", b"config"]) -> typing_extensions.Literal["redis_config", "redis_cluster_config"] | None: ...

global___Store = Store