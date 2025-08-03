# ========================================
# CHINESE LEARNING APP
# Vocabulary Practice Through Sentence Formation
# ========================================

import random
import json
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime

# ========================================
# DATA MODELS
# ========================================

@dataclass
class VocabularyWord:
    """A Chinese vocabulary word with its details"""
    chinese: str
    pinyin: str
    english: str
    example_sentence: str
    difficulty: str = "intermediate"
    category: str = "business"

@dataclass
class UserProgress:
    """Track user's learning progress"""
    user_id: str
    words_learned: List[str]
    sentences_created: List[Dict]
    current_streak: int
    total_practice_sessions: int
    last_practice_date: Optional[datetime] = None

# ========================================
# VOCABULARY DATABASE
# ========================================

VOCABULARY_DATABASE = [
    VocabularyWord(
        chinese="数据分析",
        pinyin="shù jù fēn xī",
        english="Data analysis",
        example_sentence="产品经理需要通过数据分析来了解用户行为并优化功能。",
        category="business"
    ),
    VocabularyWord(
        chinese="迭代",
        pinyin="dié dài",
        english="Iteration",
        example_sentence="为了提升用户体验，我们计划对这个功能进行多次迭代。",
        category="business"
    ),
    VocabularyWord(
        chinese="产品经理",
        pinyin="chǎn pǐn jīng lǐ",
        english="Product Manager",
        example_sentence="我们的产品经理负责制定产品战略并协调各个部门的工作。",
        category="business"
    ),
    VocabularyWord(
        chinese="垄断",
        pinyin="lǒng duàn",
        english="Monopoly",
        example_sentence="虾贝想要垄断电商市场。",
        category="business"
    ),
    VocabularyWord(
        chinese="上线",
        pinyin="shàng xiàn",
        english="Go live / Launch (a feature or product)",
        example_sentence="我们计划下周一将新功能上线。",
        category="business"
    ),
    # Additional vocabulary for variety
    VocabularyWord(
        chinese="用户体验",
        pinyin="yòng hù tǐ yàn",
        english="User experience",
        example_sentence="好的用户体验是产品成功的关键。",
        category="business"
    ),
    VocabularyWord(
        chinese="优化",
        pinyin="yōu huà",
        english="Optimize",
        example_sentence="我们需要优化这个功能以提高效率。",
        category="business"
    ),
    VocabularyWord(
        chinese="功能",
        pinyin="gōng néng",
        english="Feature / Function",
        example_sentence="这个新功能很受用户欢迎。",
        category="business"
    ),
    VocabularyWord(
        chinese="市场",
        pinyin="shì chǎng",
        english="Market",
        example_sentence="我们需要分析市场趋势来制定策略。",
        category="business"
    ),
    VocabularyWord(
        chinese="策略",
        pinyin="cè lüè",
        english="Strategy",
        example_sentence="公司制定了新的营销策略。",
        category="business"
    )
]

# ========================================
# PRAISE AND ENCOURAGEMENT MESSAGES
# ========================================

PRAISE_MESSAGES = [
    "太棒了！你的句子很有创意！🎉",
    "非常好！你很好地运用了这个词汇！👏",
    "精彩！你的句子结构很自然！✨",
    "优秀！你掌握了这个词汇的用法！🌟",
    "完美！你的句子表达得很清楚！💫",
    "了不起！你的中文进步很大！🚀",
    "出色！你很好地理解了词汇的含义！🎯",
    "棒极了！你的句子很有逻辑性！🔥",
    "太厉害了！你的表达很地道！💎",
    "精彩绝伦！你的中文水平很高！🏆"
]

ENCOURAGEMENT_MESSAGES = [
    "继续加油！每个练习都会让你进步！💪",
    "学习语言需要时间，你已经做得很好了！🌱",
    "记住，犯错是学习的一部分！保持练习！📚",
    "你的努力会带来回报的！坚持就是胜利！🎯",
    "每天进步一点点，你会越来越棒！⭐",
    "学习中文很有趣，享受这个过程！😊",
    "你的坚持会带来成功！继续努力！🌟",
    "语言学习是马拉松，不是短跑！🏃‍♂️",
    "每个新词汇都是通向流利中文的一步！🚶‍♀️",
    "相信自己，你正在变得越来越好！💫"
]

# ========================================
# CHINESE LEARNING APP
# ========================================

class ChineseLearningApp:
    """Main app for Chinese vocabulary learning through sentence formation"""
    
    def __init__(self):
        self.vocabulary = VOCABULARY_DATABASE
        self.user_progress = {}
        self.current_session_words = []
    
    def start_new_session(self, user_id: str = "default_user") -> Dict:
        """Start a new learning session with a random vocabulary word"""
        # Get a random word that hasn't been used recently
        available_words = [word for word in self.vocabulary 
                          if word.chinese not in self.current_session_words]
        
        if not available_words:
            # Reset session if all words have been used
            self.current_session_words = []
            available_words = self.vocabulary
        
        selected_word = random.choice(available_words)
        self.current_session_words.append(selected_word.chinese)
        
        # Create session data
        session_data = {
            "word": {
                "chinese": selected_word.chinese,
                "pinyin": selected_word.pinyin,
                "english": selected_word.english,
                "category": selected_word.category
            },
            "instructions": f"请使用词汇 '{selected_word.chinese}' ({selected_word.english}) 造一个句子。",
            "hint": f"提示：{selected_word.chinese} 的意思是 '{selected_word.english}'",
            "session_id": f"session_{datetime.now().timestamp()}"
        }
        
        return session_data
    
    def submit_sentence(self, user_id: str, sentence: str, word_chinese: str) -> Dict:
        """Process user's sentence submission and provide feedback"""
        # Find the vocabulary word
        word = next((w for w in self.vocabulary if w.chinese == word_chinese), None)
        
        if not word:
            return {"error": "Vocabulary word not found"}
        
        # Generate feedback
        feedback = self._generate_feedback(sentence, word)
        
        # Update user progress
        self._update_progress(user_id, word_chinese, sentence)
        
        return feedback
    
    def _generate_feedback(self, user_sentence: str, word: VocabularyWord) -> Dict:
        """Generate personalized feedback for the user's sentence"""
        # Basic validation
        if not user_sentence.strip():
            return {
                "success": False,
                "message": "请写一个句子！",
                "example_sentence": word.example_sentence,
                "encouragement": random.choice(ENCOURAGEMENT_MESSAGES)
            }
        
        # Check if the word is used in the sentence
        if word.chinese not in user_sentence:
            return {
                "success": False,
                "message": f"请在你的句子中使用词汇 '{word.chinese}'！",
                "example_sentence": word.example_sentence,
                "encouragement": random.choice(ENCOURAGEMENT_MESSAGES)
            }
        
        # Generate positive feedback
        praise = random.choice(PRAISE_MESSAGES)
        
        return {
            "success": True,
            "message": praise,
            "user_sentence": user_sentence,
            "example_sentence": word.example_sentence,
            "word_analysis": {
                "chinese": word.chinese,
                "pinyin": word.pinyin,
                "english": word.english,
                "usage_tip": self._generate_usage_tip(word)
            },
            "encouragement": random.choice(ENCOURAGEMENT_MESSAGES)
        }
    
    def _generate_usage_tip(self, word: VocabularyWord) -> str:
        """Generate a helpful tip about using the word"""
        tips = {
            "数据分析": "数据分析通常用于描述分析数据的过程，可以搭配'进行'、'做'等动词。",
            "迭代": "迭代常用于描述产品开发过程，可以搭配'进行'、'完成'等动词。",
            "产品经理": "产品经理是职位名称，通常用作主语或宾语。",
            "垄断": "垄断通常用作动词，表示独占市场的行为。",
            "上线": "上线是动词，表示产品或功能正式发布，可以搭配'将'、'计划'等词。",
            "用户体验": "用户体验是名词，通常用作主语或宾语。",
            "优化": "优化是动词，表示改进或提升，可以搭配'进行'、'完成'等动词。",
            "功能": "功能是名词，表示产品的特性，可以搭配'开发'、'测试'等动词。",
            "市场": "市场是名词，表示商业环境，可以搭配'分析'、'进入'等动词。",
            "策略": "策略是名词，表示计划或方法，可以搭配'制定'、'执行'等动词。"
        }
        return tips.get(word.chinese, "这个词汇可以根据语境灵活使用。")
    
    def _update_progress(self, user_id: str, word_chinese: str, sentence: str):
        """Update user's learning progress"""
        if user_id not in self.user_progress:
            self.user_progress[user_id] = UserProgress(
                user_id=user_id,
                words_learned=[],
                sentences_created=[],
                current_streak=0,
                total_practice_sessions=0
            )
        
        progress = self.user_progress[user_id]
        
        # Add word to learned list if not already there
        if word_chinese not in progress.words_learned:
            progress.words_learned.append(word_chinese)
        
        # Add sentence to created sentences
        progress.sentences_created.append({
            "word": word_chinese,
            "sentence": sentence,
            "timestamp": datetime.now().isoformat()
        })
        
        # Update streak and sessions
        progress.current_streak += 1
        progress.total_practice_sessions += 1
        progress.last_practice_date = datetime.now()
    
    def get_user_progress(self, user_id: str) -> Dict:
        """Get user's learning progress"""
        if user_id not in self.user_progress:
            return {
                "words_learned": 0,
                "sentences_created": 0,
                "current_streak": 0,
                "total_sessions": 0,
                "message": "开始你的中文学习之旅吧！"
            }
        
        progress = self.user_progress[user_id]
        return {
            "words_learned": len(progress.words_learned),
            "sentences_created": len(progress.sentences_created),
            "current_streak": progress.current_streak,
            "total_sessions": progress.total_practice_sessions,
            "recent_sentences": progress.sentences_created[-5:] if progress.sentences_created else [],
            "message": f"你已经学习了 {len(progress.words_learned)} 个词汇，创造了 {len(progress.sentences_created)} 个句子！"
        }
    
    def get_vocabulary_list(self) -> List[Dict]:
        """Get all vocabulary words for reference"""
        return [
            {
                "chinese": word.chinese,
                "pinyin": word.pinyin,
                "english": word.english,
                "category": word.category,
                "example_sentence": word.example_sentence
            }
            for word in self.vocabulary
        ]

# ========================================
# INTERACTIVE DEMO
# ========================================

def run_interactive_demo():
    """Run an interactive demo of the Chinese learning app"""
    print("🇨🇳 中文学习应用 - 词汇造句练习")
    print("=" * 50)
    
    app = ChineseLearningApp()
    user_id = "demo_user"
    
    print("\n欢迎来到中文学习应用！")
    print("我们将通过造句练习来帮助你学习中文词汇。")
    print("每个练习都会给你一个词汇，请用它造一个句子。")
    
    while True:
        print("\n" + "="*50)
        
        # Start new session
        session = app.start_new_session(user_id)
        word = session["word"]
        
        print(f"\n📚 新练习")
        print(f"词汇: {word['chinese']}")
        print(f"拼音: {word['pinyin']}")
        print(f"意思: {word['english']}")
        print(f"提示: {session['hint']}")
        
        # Get user input
        user_sentence = input(f"\n请用 '{word['chinese']}' 造一个句子: ")
        
        if user_sentence.lower() in ['quit', 'exit', '退出', 'q']:
            print("\n谢谢使用中文学习应用！再见！👋")
            break
        
        # Process submission
        feedback = app.submit_sentence(user_id, user_sentence, word['chinese'])
        
        print(f"\n📝 你的句子: {user_sentence}")
        
        if feedback["success"]:
            print(f"✅ {feedback['message']}")
            print(f"📖 示例句子: {feedback['example_sentence']}")
            print(f"💡 使用提示: {feedback['word_analysis']['usage_tip']}")
        else:
            print(f"❌ {feedback['message']}")
            print(f"📖 示例句子: {feedback['example_sentence']}")
        
        print(f"💪 {feedback['encouragement']}")
        
        # Show progress
        progress = app.get_user_progress(user_id)
        print(f"\n📊 学习进度:")
        print(f"   已学词汇: {progress['words_learned']}")
        print(f"   造句数量: {progress['sentences_created']}")
        print(f"   连续练习: {progress['current_streak']} 次")
        
        # Ask if user wants to continue
        continue_choice = input(f"\n继续练习？(y/n): ").lower()
        if continue_choice not in ['y', 'yes', '是', '继续']:
            print("\n谢谢使用中文学习应用！再见！👋")
            break
    
    # Final progress summary
    final_progress = app.get_user_progress(user_id)
    print(f"\n🎉 学习总结:")
    print(f"   总共学习了 {final_progress['words_learned']} 个词汇")
    print(f"   创造了 {final_progress['sentences_created']} 个句子")
    print(f"   完成了 {final_progress['total_sessions']} 次练习")
    print(f"   连续练习了 {final_progress['current_streak']} 次")
    
    if final_progress['recent_sentences']:
        print(f"\n📝 最近的句子:")
        for i, sentence_data in enumerate(final_progress['recent_sentences'][-3:], 1):
            print(f"   {i}. {sentence_data['word']}: {sentence_data['sentence']}")

def show_vocabulary_reference():
    """Show all vocabulary words for reference"""
    print("\n📚 词汇参考表")
    print("=" * 50)
    
    app = ChineseLearningApp()
    vocabulary_list = app.get_vocabulary_list()
    
    for i, word in enumerate(vocabulary_list, 1):
        print(f"\n{i}. {word['chinese']} ({word['pinyin']})")
        print(f"   意思: {word['english']}")
        print(f"   分类: {word['category']}")
        print(f"   例句: {word['example_sentence']}")

if __name__ == "__main__":
    print("选择模式:")
    print("1. 交互式练习")
    print("2. 查看词汇表")
    
    choice = input("请输入选择 (1 或 2): ")
    
    if choice == "1":
        run_interactive_demo()
    elif choice == "2":
        show_vocabulary_reference()
    else:
        print("无效选择，运行交互式练习...")
        run_interactive_demo() 