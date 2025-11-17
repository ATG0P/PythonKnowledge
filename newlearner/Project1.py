import numpy as np

nrg = np.random.default_rng()

# Generate each column
subject_data = nrg.integers(45, 101, size=(1000, 3))       # 1000 rows, 3 subjects
id_data = nrg.integers(1000000, 10000000, size=(1000, 1))  # IDs
attendance_data = nrg.integers(60, 101, size=(1000, 1))    # Attendance

# Combine all columns into a final dataset
Final_Data = np.hstack([id_data, subject_data, attendance_data])

print(Final_Data)
