"""聚合物温度模拟脚本

模拟放热聚合反应中反应器温度随时间的变化（含冷却），并使用 Fox 方程
计算共聚物的玻璃化转变温度 Tg。

模型：
    - 反应速率遵循 Arrhenius 方程: k(T) = A * exp(-Ea / (R*T))
    - 单体转化率: dX/dt = k(T) * (1 - X)
    - 能量平衡: dT/dt = (Q_reaction - Q_cooling) / (m * Cp)
        Q_reaction = ΔH * m * dX/dt          (放热)
        Q_cooling  = U * A * (T - T_cool)    (夹套冷却)
    - 共聚物 Tg (Fox 方程): 1/Tg = w1/Tg1 + w2/Tg2
"""

import numpy as np
import matplotlib.pyplot as plt

# 配置中文字体（Windows 上 Microsoft YaHei 支持中文）
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False


def fox_tg(w1, tg1, w2, tg2):
    """Fox 方程计算共聚物玻璃化转变温度 (K)。

    参数:
        w1, w2 : 两组分质量分数 (w1 + w2 == 1)
        tg1, tg2 : 两组分均聚物 Tg (K)
    """
    return 1.0 / (w1 / tg1 + w2 / tg2)


def simulate_polymerization(
    T0=320.0,          # 初始温度 (K)
    monomer_mass=1.0,  # 单体质量 (kg)
    Cp=1.8,            # 比热容 (kJ/(kg·K))
    dH=-80.0,          # 反应焓 (kJ/kg，负号表示放热)
    A=3.0e8,           # 指前因子 (1/s)
    Ea=60.0,           # 活化能 (kJ/mol)
    U_A=0.02,          # 冷却换热 UA (kW/K)
    T_cool=300.0,      # 冷却介质温度 (K)
    t_end=600.0,       # 模拟时长 (s)
    dt=0.2,            # 时间步长 (s)
):
    R = 8.314e-3  # 气体常数 (kJ/(mol·K))
    n_steps = int(t_end / dt)
    t = np.zeros(n_steps + 1)
    T = np.zeros(n_steps + 1)
    X = np.zeros(n_steps + 1)

    T[0] = T0
    X[0] = 0.0

    for i in range(n_steps):
        k = A * np.exp(-Ea / (R * T[i]))          # 反应速率常数 (1/s)
        dXdt = k * (1.0 - X[i])                    # 转化率变化率
        Q_rxn = -dH * monomer_mass * dXdt          # 反应放热功率 (kW)
        Q_cool = U_A * (T[i] - T_cool)             # 冷却功率 (kW)
        dTdt = (Q_rxn - Q_cool) / (monomer_mass * Cp)
        t[i + 1] = t[i] + dt
        X[i + 1] = X[i] + dXdt * dt
        T[i + 1] = T[i] + dTdt * dt

    return t, T, X


def plot_results(t, T, X, Tg=None):
    fig, ax1 = plt.subplots(figsize=(8, 5))
    ax1.plot(t, T, color="crimson", label="反应温度 T(t)")
    ax1.set_xlabel("时间 (s)")
    ax1.set_ylabel("温度 (K)", color="crimson")
    ax1.tick_params(axis="y", labelcolor="crimson")

    ax2 = ax1.twinx()
    ax2.plot(t, X, color="steelblue", label="转化率 X(t)")
    ax2.set_ylabel("转化率", color="steelblue")
    ax2.tick_params(axis="y", labelcolor="steelblue")
    ax2.set_ylim(0, 1.05)

    if Tg is not None:
        ax1.axhline(Tg, color="green", linestyle="--", linewidth=1.2,
                    label=f"共聚物 Tg ≈ {Tg:.1f} K")
        ax1.legend(loc="upper right")

    plt.title("聚合反应温度与转化率模拟")
    fig.tight_layout()
    out = "polymer_temperature.png"
    plt.savefig(out, dpi=120)
    print(f"图表已保存: {out}")


def main():
    print("=" * 60)
    print("聚合物温度模拟")
    print("=" * 60)

    # 1. 共聚物 Tg —— 苯乙烯/丁二烯为例
    tg_styrene = 378.0   # PS 的 Tg (K) ≈ 105 °C
    tg_butadiene = 178.0 # PB 的 Tg (K) ≈ -95 °C
    w_s, w_b = 0.7, 0.3
    Tg = fox_tg(w_s, tg_styrene, w_b, tg_butadiene)
    print(f"\n[共聚物 Tg - Fox 方程]")
    print(f"  苯乙烯 w={w_s}, Tg={tg_styrene} K")
    print(f"  丁二烯 w={w_b}, Tg={tg_butadiene} K")
    print(f"  共聚物 Tg ≈ {Tg:.2f} K  ({Tg - 273.15:.2f} °C)")

    # 2. 反应器温度模拟
    print(f"\n[反应器温度模拟]")
    t, T, X = simulate_polymerization()
    print(f"  初始温度 T0 = {T[0]:.2f} K")
    print(f"  最高温度 Tmax = {T.max():.2f} K  (温升 {T.max() - T[0]:.2f} K)")
    print(f"  最终温度 = {T[-1]:.2f} K")
    print(f"  最终转化率 = {X[-1]:.4f}")
    if T.max() >= Tg:
        print(f"  ⚠ 放热峰 {T.max():.1f} K 超过共聚物 Tg {Tg:.1f} K，"
              f"注意凝胶效应（Trommsdorff 自动加速）/粘度激增")

    plot_results(t, T, X, Tg=Tg)
    print("\n完成。")


if __name__ == "__main__":
    main()
