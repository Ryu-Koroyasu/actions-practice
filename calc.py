def average(nums: list[float]) -> float:
    """数値のリストの平均を返す。

    Args:
        nums: 平均を取る数値のリスト。

    Returns:
        平均値。

    Raises:
        ValueError: リストが空のとき。
    """
    if not nums:
        raise ValueError("空のリストの平均は計算できません")
    return sum(nums) / len(nums)
