import openai

# OpenAI API 키 설정
openai.api_key = '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'

# 직무 분야에 따른 질문 생성 프롬프트
def generate_questions_for_field(field):
    prompt = (
        f"다음 직무 분야에 적합한 인터뷰 질문을 3개 만들어 주세요: {field}\n"
        "질문을 번호와 함께 나열해 주세요."
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 또는 gpt-4 사용 가능
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 또는 gpt-4 사용 가능
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()

def evaluate_response(question, response):
    # 질문과 답변의 상관관계를 평가하는 프롬프트 생성
    evaluation_prompt = (
        f"질문: {question}\n"
        f"답변: {response}\n\n"
        "위의 질문과 답변이 얼마나 관련이 있는지 평가해 주세요. "
        "다음 중 하나로 평가하세요: '상', '중', '하'. "
        "평가의 기준은 답변이 질문에 얼마나 잘 맞는지입니다."
    )

    evaluation_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 또는 gpt-4 사용 가능
        messages=[{"role": "user", "content": evaluation_prompt}],
        max_tokens=10
    )

    return evaluation_response.choices[0].message['content'].strip()

# 인터뷰 시뮬레이터
def interview_simulator():
    print("인터뷰 시뮬레이터에 오신 것을 환영합니다.")

    # 분야 선택
    field = input("직무 분야를 입력해주세요 (예: 소프트웨어 개발, 마케팅, 디자인 등): ")

    if not field.strip():
        print("직무 분야를 입력해주세요.")
        return

    # 해당 분야에 맞는 질문 생성
    questions_prompt = generate_questions_for_field(field)
    questions = questions_prompt.split('\n')

    print("다음 질문들 중 하나를 선택하세요:")
    for idx, question in enumerate(questions):
        print(f"{idx + 1}. {question}")

    question_index = int(input("질문 번호를 선택하세요: ")) - 1
    if question_index < 0 or question_index >= len(questions):
        print("잘못된 번호입니다. 프로그램을 종료합니다.")
        return

    selected_question = questions[question_index]
    print(f"선택된 질문: {selected_question}\n")

    # 답변 생성 및 평가
    prompt = f"당신은 인터뷰 대상자입니다. 다음 질문에 대답하세요: {selected_question}"
    response = generate_response(prompt)
    print(f"답변: {response}\n")

    # 답변 평가
    evaluation = evaluate_response(selected_question, response)
    print(f"답변 평가: {evaluation}\n")

interview_simulator()
