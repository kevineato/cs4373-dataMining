# Kevin wilson syx009
# generate first csv containing ranges
echo 'department,age,salary,status' > hwk03.csv

for (( i = 0; i < 30; i++ )); do
  echo 'sales,31..35,46k..50k,senior' >> hwk03.csv
done

for (( i = 0; i < 40; i++ )); do
  echo 'sales,26..30,26k..30k,junior' >> hwk03.csv
done

for (( i = 0; i < 40; i++ )); do
  echo 'sales,31..35,31k..35k,junior' >> hwk03.csv
done

for (( i = 0; i < 20; i++ )); do
  echo 'systems,21..25,46k..50k,junior' >> hwk03.csv
done

for (( i = 0; i < 5; i++ )); do
  echo 'systems,31..35,66k..70k,senior' >> hwk03.csv
done

for (( i = 0; i < 3; i++ )); do
  echo 'systems,26..30,46k..50k,junior' >> hwk03.csv
done

for (( i = 0; i < 3; i++ )); do
  echo 'systems,41..45,66k..70k,senior' >> hwk03.csv
done

for (( i = 0; i < 10; i++ )); do
  echo 'marketing,36..40,46k..50k,senior' >> hwk03.csv
done

for (( i = 0; i < 4; i++ )); do
  echo 'marketing,31..35,41k..45k,junior' >> hwk03.csv
done

for (( i = 0; i < 4; i++ )); do
  echo 'secretary,46..50,36k..40k,senior' >> hwk03.csv
done

for (( i = 0; i < 6; i++ )); do
  echo 'secretary,26..30,26k..30k,junior' >> hwk03.csv
done

# generate second csv containing random values in ranges
echo 'department,age,salary,status' > hwk03-02.csv

for (( i = 0; i < 30; i++ )); do
  echo "sales,$((31 + RANDOM % 5)),$((46 + RANDOM % 5))k,senior" >> hwk03-02.csv
done

for (( i = 0; i < 40; i++ )); do
  echo "sales,$((26 + RANDOM % 5)),$((26 + RANDOM % 5))k,junior" >> hwk03-02.csv
done

for (( i = 0; i < 40; i++ )); do
  echo "sales,$((31 + RANDOM % 5)),$((31 + RANDOM % 5))k,junior" >> hwk03-02.csv
done

for (( i = 0; i < 20; i++ )); do
  echo "systems,$((21 + RANDOM % 5)),$((46 + RANDOM % 5))k,junior" >> hwk03-02.csv
done

for (( i = 0; i < 5; i++ )); do
  echo "systems,$((31 + RANDOM % 5)),$((66 + RANDOM % 5))k,senior" >> hwk03-02.csv
done

for (( i = 0; i < 3; i++ )); do
  echo "systems,$((26 + RANDOM % 5)),$((46 + RANDOM % 5))k,junior" >> hwk03-02.csv
done

for (( i = 0; i < 3; i++ )); do
  echo "systems,$((41 + RANDOM % 5)),$((66 + RANDOM % 5))k,senior" >> hwk03-02.csv
done

for (( i = 0; i < 10; i++ )); do
  echo "marketing,$((36 + RANDOM % 5)),$((46 + RANDOM % 5))k,senior" >> hwk03-02.csv
done

for (( i = 0; i < 4; i++ )); do
  echo "marketing,$((31 + RANDOM % 5)),$((41 + RANDOM % 5))k,junior" >> hwk03-02.csv
done

for (( i = 0; i < 4; i++ )); do
  echo "secretary,$((46 + RANDOM % 5)),$((36 + RANDOM % 5))k,senior" >> hwk03-02.csv
done

for (( i = 0; i < 6; i++ )); do
  echo "secretary,$((26 + RANDOM % 5)),$((26 + RANDOM % 5))k,junior" >> hwk03-02.csv
done