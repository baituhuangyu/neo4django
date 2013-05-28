options={
	}
tests=[
	'test_get_or_create',
	'test_json_serialize',
	'test_unique',
	'test_default_parents_index',
	'test_indexed_types',
	'test_create',
	'test_delete',
	'test_iter',
	'test_dates',
	'test_all',
	'test_get',
	'test_filter_exact',
	'test_filter_iexact',
	'test_filter_range',
	'test_exclude_exact',
	'test_basic_relationship',
	'test_one_to_many',
	'test_many_to_one',
	'test_related_one_to_many',
	'test_related_many_to_one',
	'test_one_to_one',
	'test_ordering',
	'test_relationship_model',
	'test_multinode_setting',
	'test_save_delete',
	'test_custom_clients_same_database',
	'test_prop',
	'test_none_prop',
	'test_integer',
	'test_date_constructor',
	'test_date_prop',
	'test_datetime_constructor',
	'test_datetime_auto_now',
	'test_datetime_auto_now_add',
	'test_date_auto_now',
	'test_date_auto_now_add',
	'test_type_nodes',
	'test_model_inheritance',
	'test_nodemodel_independence',
	'test_array_property_validator',
	'test_int_array_property',
	'test_str_array_property_validator',
	'test_url_array_property_validator',
	'test_basic_indexed_query',
	'test_negated_query',
	'test_unindexed_query',
	'test_complex_query',
	'test_type_query',
	'test_filter_gt',
	'test_filter_gte',
	'test_filter_lt',
	'test_filter_lte',
	'test_filter_date_range',
	'test_model_casting',
	'test_model_casting_validation',
	'test_model_copy',
	'test_basic_relationship_manager',
	'test_one_to_one',
	'test_rel_metadata',
	'test_prop_metadata',
	'test_rel_self',
	'test_rel_string_target',
	'test_auto_property',
	'test_rel_string_type',
	'test_get_by_id',
	'test_in_id',
	'test_empty_array',
	'test_typenode_transactionality',
	'test_queryset_str',
	'test_in_bulk',
	'test_auto_property_indexing',
	'test_filter_array_member',
	'test_autoproperty_transactionality',
	'test_abstract_rel_inheritance',
	'test_filter_in',
	'test_filter_contains',
	'test_filter_startswith',
	'test_datetime_auto_now_add',
	'test_select_related',
	'test_rel_query_direction',
	'test_filter_array_member_in',
	'test_large_query',
	'test_zerovalued_lookup',
	'test_datetimetz_constructor',
	'test_datetimetz_prop',
	'test_datetime_prop',
	'test_custom_manager',
	'test_other_library',
	'test_rel_slicing',
	'test_pre_init',
	'test_post_init',
	'test_pre_save',
	'test_post_save',
	'test_pre_delete',
	'test_post_delete',
	'test_in_bulk_not_found',
	'test_none',
	'test_relationship_none',
	'test_relationship_count',
	'test_relationship_filter',
	'test_cleandb',
	'test_object_index',
	'test_array_use_strings',
	'test_array_use_strings_value_escaping',
	'test_relationship_create',
	'test_relationship_delete',
	'test_rel_cache',
	'test_conflicting_rel_types',
	'test_syncdb',
	'test_model_pickling',
	'touch_test_db',
	'rm_test_db',
	'test_spanning_lookup',
	'test_order_by',
	'test_count',
	'test_aggregate_count',
	'test_exists',
	'test_aggregate_avg',
	'test_aggregate_sum',
	'test_aggregate_max_min',
	'test_auth',
	'test_auth_backend',
	'test_modelform',
	'test_query_type',
	'test_complex_filters',
	'test_inherited_indexed_filter',
	'test_spanning_lookup',
	'test_related_modelform',
	'test_relationship_models',
	'test_relationship_distinct',
	'test_reverse',
	'test_latest',
	'test_filter_icontains',
	'test_filter_istartswith',
	'test_filter_iregex',
	'test_filter_regex',
	'test_filter_iendswith',
	'test_filter_endswith',
	'test_filter_year',
	'test_filter_month',
	'test_filter_day']
should_fail=[
	'test_dates',
	'test_relationship_model',
	'test_nodemodel_independence',
	'test_url_array_property_validator',
	'test_type_query',
	'test_model_casting_validation',
	'test_array_use_strings',
	'test_relationship_models',
	'test_filter_year',
	'test_filter_month',
	'test_filter_day']
