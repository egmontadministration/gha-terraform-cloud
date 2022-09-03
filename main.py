import config
import tfcloud


if __name__ == '__main__':
    conf = config.load_config()

    module_exists = tfcloud.check_module_exists(
        conf['tfc_organization'],
        conf['tfc_token'],
        conf['gh_organization'],
        conf['gh_repository']
    )

    if module_exists:
        print('Module {} is already registered'.format(conf['gh_repository']))
        exit(0)

    tfcloud.register_module(
        conf['tfc_organization'],
        conf['tfc_token'],
        conf['tfc_client_name'],
        conf['gh_organization'],
        conf['gh_repository']
    )

    print('Module {} has been registered'.format(conf['gh_repository']))
