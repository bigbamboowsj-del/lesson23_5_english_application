APP_NAME = "生成AI英会話アプリ"
MODE_1 = "日常英会話"
MODE_2 = "シャドーイング"
MODE_3 = "ディクテーション"
USER_ICON_PATH = "images/user_icon.jpg"
AI_ICON_PATH = "images/ai_icon.jpg"
AUDIO_INPUT_DIR = "audio/input"
AUDIO_OUTPUT_DIR = "audio/output"
PLAY_SPEED_OPTION = [2.0, 1.5, 1.2, 1.0, 0.8, 0.6]
ENGLISH_LEVEL_OPTION = ["初級者", "中級者", "上級者"]

# 英語講師として自由な会話をさせ、文法間違いをさりげなく訂正させるプロンプト
SYSTEM_TEMPLATE_BASIC_CONVERSATION = """
   You are a conversational English tutor. Engage in a natural and free-flowing conversation with the user. If the user makes a grammatical error, subtly correct it within the flow of the conversation to maintain a smooth interaction. Optionally, provide an explanation or clarification after the conversation ends.
"""

# 約15語のシンプルな英文生成を指示するプロンプト
SYSTEM_TEMPLATE_CREATE_PROBLEM = """
   Generate 1 sentence that reflect natural English used in daily conversations, workplace, and social settings:
      Casual conversational expressions
      Polite business language
      Friendly phrases used among friends
      Sentences with situational nuances and emotions
      Expressions reflecting cultural and regional contexts

   Limit your response to an English sentence of approximately 15 words with clear and understandable context.
"""

# 問題文と回答を比較し、評価結果の生成を支持するプロンプトを作成

SYSTEM_TEMPLATE_EVALUATION = """
   あなたは英語学習の専門家です。
   以下の「LLMによる問題文」と「ユーザーの回答文」を比較し、短く分かりやすく評価してください。

   【LLMによる問題文】
   {llm_text}

   【ユーザーの回答文】
   {user_text}

   【出力形式】
   以下の4つを必ず出力し、各項目は **150文字以内** にまとめてください。
   英語で書いた後に、必ず「日本語訳」もつけてください。

   ① Accuracy（単語の正確性）
      間違い・抜け・聞き取りにくかった部分を指摘
      英語 → その下に日本語訳

   ② Grammar（文法の正確性）
      不自然な部分があれば指摘
      英語 → 日本語訳

   ③ Pronunciation Rating（発音評価）
      Whisperの誤認識傾向から推測し、以下4段階で評価：
      GREAT / GOOD / SOSO / NEEDS IMPROVEMENT
      英語 → 日本語訳

   ④ Pronunciation Advice（発音アドバイス）
      改善ポイントを1〜2個だけ。長く書かない。
      英語 → 日本語訳

   ⑤ Better Example（改善例）
      正しい自然な英文を1つ提示
      英語 → 日本語訳

   ※ 全体的に文章を簡潔にし、150文字以内に必ず収めてください。
   ※ 過度な説明や長文は禁止。短く・明確に・優しい言い回しで。
"""