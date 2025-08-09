from typing import Any

from ninja import Router
import requests

triple_luck_router = Router()


@triple_luck_router.get("/get-triple-luck-page", tags=["triple_luck"])
def get_triple_luck_page(request: Any) -> dict[str, str]:
    """
    get triple luck page API
    ```
    Args:
        request (Any): request object

    Returns:
        dict[str, str]: health check response
        - status: ok
        - timestamp: current timestamp
    ```
    """
    url = "https://dhlottery.co.kr/gameInfo.do?method=lottoMainView&lottoId=LI21"
    resp = requests.get(url, timeout=10)
    resp.encoding = "euc-kr"  # EUC-KR 인코딩 지정
    if resp.status_code != 200:
        return {
            "error": "Failed to fetch the page"
        }
    return {
        "html": resp.text
        }
