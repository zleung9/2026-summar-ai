"""从聚合物字典计算数量与平均玻璃化转变温度（Tg）。

本脚本读取一个“聚合物名 -> Tg(摄氏度)”的字典，输出聚合物的数量
和它们的平均 Tg。
"""

POLYMERS = {
    "PE": -125,
    "PS": 100,
    "PET": 70,
}


def average_tg(polymer_data):
    """返回给定聚合物的平均玻璃化转变温度。空字典返回 None。"""
    if not polymer_data:
        return None
    return sum(polymer_data.values()) / len(polymer_data)


def main():
    """打印聚合物数量与平均 Tg。"""
    num_polymers = len(POLYMERS)
    mean_tg = average_tg(POLYMERS)

    print(f"聚合物数量：{num_polymers}")
    if mean_tg is None:
        print("平均 Tg：无数据（空字典）")
    else:
        print(f"聚合物平均 Tg：{mean_tg:.1f} C")


if __name__ == "__main__":
    main()
