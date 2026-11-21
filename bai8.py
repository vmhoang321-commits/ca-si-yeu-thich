import streamlit as st

with st.sidebar:
    image = "mili.jpg"
    st.image(image, caption = "Momocashew")
    st.write("Họ và Tên: Cassie Wei")
    st.write("Nhóm: Momocashew")
    st.write("Cassie Wei, là giọng ca chính, người viết lời và đồng sáng lập của Mili." \
    " Cô được biết đến với chất giọng trong trẻo, ma mị nhưng đầy nội lực.Tiểu sử. " \
    "Sinh ngày 8 tháng 5 năm 1993 tại Bắc Kinh (Trung Quốc) và lớn lên ở Canada. Cô thông thạo ba ngôn ngữ: tiếng Trung, tiếng Anh và tiếng Nhật." \
    "Phong cách sáng tác. Lời bài hát của Cassie thường lấy cảm hứng từ cuộc sống hằng ngày, các nghiên cứu lịch sử, văn học và tâm lý học, biến mỗi ca khúc thành một câu chuyện ngắn giàu hình ảnh.")

st.title("Bài hát yêu thích")
st.write("SAIKAI")
audio = open("SAIKAI.mp3","rb")
st.audio(audio,format = 'audio/mp3')

st.title("MV yêu thích")
st.title("City Blue")
video = 'https://www.youtube.com/watch?v=dUThbdoat00'
st.video(video,format = 'video/mp4')