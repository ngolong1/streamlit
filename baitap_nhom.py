import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
movies_data = pd.read_csv("https://raw.githubusercontent.com/nv-thang/Data-Visualization-Course/main/Dataset%20for%20Practice/movies.csv")

# Tùy chọn hiển thị
option = st.selectbox(
    "Chọn cách hiển thị:",
    ["Toàn bộ theo thể loại", "Lọc theo năm"]
)

# Hiển thị dữ liệu mẫu
st.write("📋 Dữ liệu mẫu:")
st.dataframe(movies_data.head())

# Lọc dữ liệu nếu chọn theo năm
if option == "Lọc theo năm":
    selected_year = st.selectbox("Chọn năm:", sorted(movies_data['year'].dropna().unique()))
    filtered_data = movies_data[movies_data['year'] == selected_year]
    st.write(f"🎬 Dữ liệu cho năm {selected_year}")
else:
    filtered_data = movies_data

# Ngân sách trung bình theo thể loại
st.write("💰 Ngân sách trung bình theo thể loại phim")
avg_budget = filtered_data.groupby('genre')['budget'].mean().round().reset_index()

fig = plt.figure(figsize=(19, 10))
bars = plt.bar(avg_budget['genre'], avg_budget['budget'], color='maroon')
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{height:.0f}', ha='center', va='bottom')

plt.xlabel('Thể loại phim')
plt.ylabel('Ngân sách trung bình')
plt.title('Average Movie Budget by Genre')
plt.xticks(rotation=45)
st.pyplot(fig)

# Doanh thu trung bình theo thể loại
avg_gross = filtered_data.groupby('genre')['gross'].mean().round().reset_index()
fig1 = plt.figure(figsize=(19, 10))
plt.bar(avg_gross['genre'], avg_gross['gross'], color='darkgreen')
plt.xlabel('Thể loại phim')
plt.ylabel('Doanh thu trung bình')
plt.title('Average Movie Gross Revenue by Genre')
plt.xticks(rotation=45)
st.write("💸 Doanh thu trung bình theo thể loại phim")
st.pyplot(fig1)

# Thời lượng trung bình theo thể loại
avg_runtime = filtered_data.groupby('genre')['runtime'].mean().round().reset_index()
fig2 = plt.figure(figsize=(19, 10))
plt.plot(avg_runtime['genre'], avg_runtime['runtime'], marker='o', linestyle='-', color='orange')
plt.xlabel('Thể loại phim')
plt.ylabel('Thời lượng trung bình (phút)')
plt.title('Xu hướng thời lượng trung bình theo thể loại')
plt.xticks(rotation=45)
st.write("⏱️ Xu hướng thời lượng trung bình phim theo thể loại")
st.pyplot(fig2)


