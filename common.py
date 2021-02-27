import constantKeeper as keeper
import vk_api


def authorizeAndGetAPI(scope) -> vk_api.VkApi:
    vk_session = vk_api.VkApi(keeper.MY_LOGIN, keeper.MY_PASSWORD)
    vk_session.auth()
    return vk_session.get_api()




