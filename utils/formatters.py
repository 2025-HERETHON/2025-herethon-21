from datetime import datetime

def format_timestamp(time:datetime):
    """
    주어진 일시 값을 특정 형식으로 변환합니다.
    Args:
        time(datetime): 일시
    Returns:
        str: 타임스탬프 (예: '2025-07-08_14:40:00_Asia/Seoul')
    """
    return time.strftime(f'%Y-%m-%d_%H:%M:%S_{time.tzinfo}')