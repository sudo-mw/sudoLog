
def example_slicing_basic():
    """기본 슬라이싱: 시작과 끝 지정"""
    text = "Hello World"
    # 'Hello'만 추출 (0~4번 인덱스)
    result = text[0:5]
    print(f"Basic: {result}")

def example_negative_slicing():
    """음수 인덱스: 뒤에서부터 추출"""
    text = "Hello World"
    # 뒤에서 5글자 'World' 추출
    result = text[-5:]
    print(f"Negative: {result}")

def example_step_slicing():
    """단계 설정: 간격 조절 및 뒤집기"""
    text = "ABCDEFG"
    # 한 칸씩 건너뛰기
    step = text[::2]
    # 문자열 뒤집기
    reverse = text[::-1]
    print(f"Step: {step}, Reverse: {reverse}")

if __name__ == "__main__":
    example_slicing_basic()
    example_negative_slicing()
    example_step_slicing()