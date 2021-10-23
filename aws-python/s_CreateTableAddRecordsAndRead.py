import serverless_sdk
sdk = serverless_sdk.SDK(
    org_id='aadiupa',
    application_name='aws-python',
    app_uid='4M9r4xL5z0mkwhqBxT',
    org_uid='f66bfa87-3590-4e59-915e-39e570eb2b74',
    deployment_uid='e9f9375d-7b13-42b5-ae61-28706805ea29',
    service_name='aws-python',
    should_log_meta=True,
    should_compress_logs=True,
    disable_aws_spans=False,
    disable_http_spans=False,
    stage_name='dev',
    plugin_version='5.5.0',
    disable_frameworks_instrumentation=False,
    serverless_platform_stage='prod'
)
handler_wrapper_kwargs = {'function_name': 'aws-python-dev-CreateTableAddRecordsAndRead', 'timeout': 3}
try:
    user_handler = serverless_sdk.get_user_handler('app.handler')
    handler = sdk.handler(user_handler, **handler_wrapper_kwargs)
except Exception as error:
    e = error
    def error_handler(event, context):
        raise e
    handler = sdk.handler(error_handler, **handler_wrapper_kwargs)
