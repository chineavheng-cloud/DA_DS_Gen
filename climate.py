import numpy as np
climate_data = np.load("climate_data.npy")
print("Shape:", climate_data.shape)
print("Dimensions:", climate_data.ndim)
print("Data type:", climate_data.dtype)
baseline_grid = np.zeros((climate_data.shape[0], climate_data.shape[1]))
region = climate_data[20:50, 70:120, :]
day_15 = climate_data[:, :, 14]
clean_data = climate_data.astype(float)
mask = clean_data == -99
clean_data[mask] = np.nan
fahrenheit_data = (clean_data * 9/5) + 32
heat_stress = np.exp(clean_data / 30) + np.log(clean_data + 1)
max_temp = np.nanmax(clean_data)
min_temp = np.nanmin(clean_data)
print("Highest temperature:", max_temp)
print("Lowest temperature:", min_temp)
avg_temp_map = np.nanmean(clean_data, axis=2)
print("Average temperature map shape:", avg_temp_map.shape)