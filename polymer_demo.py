# polymer_demo.py
import numpy as np
import matplotlib.pyplot as plt

def calculate_tg(chain_length, monomer_weight, k=0.5):
    # 故意留了一个 Bug：用数组作为索引，运行会报 TypeError
    return k * np.sqrt(chain_length) * monomer_weight

def main():
    chain_lengths = np.array([10, 50, 100, 200])
    monomer_weights = np.array([100, 120, 150, 180])
    
    print("开始计算聚合物 Tg...")
    tg_values = calculate_tg(chain_lengths, monomer_weights)
    
    plt.plot(chain_lengths, tg_values, 'o-')
    plt.xlabel('链长 (重复单元)')
    plt.ylabel('Tg (°C)')
    plt.title('聚合物玻璃化转变温度')
    plt.grid(True)
    plt.savefig('tg_plot.png')
    print("图表已保存为 tg_plot.png")
    print(f"Tg 值: {tg_values}")

if __name__ == "__main__":
    main()
