import linear_regress
import numpy as np

print("Starting FPS Approx Prog... Enter cpu_bench, gpu_bench, cpu_core, cpu_thread, gpu_mem, gpu_clk_boost")

cpu_bench, gpu_bench, cpu_core, cpu_thread, gpu_mem, gpu_clk_boost = input(": ").split()

input_data = [cpu_bench, gpu_bench, cpu_core, cpu_thread, gpu_mem, gpu_clk_boost]

cpu_data = list(np.array(input_data, dtype = 'float64'))

Frame1, Frame2, Frame3 = linear_regress.getApproxFrame(cpu_data)

frame = [Frame1, Frame2, Frame3]

linear_regress.addData(cpu_data, frame)