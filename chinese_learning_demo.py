# ========================================
# CHINESE LEARNING APP DEMO
# Shows how the app works without interactive input
# ========================================

import random
from datetime import datetime
from chinese_learning_app import ChineseLearningApp, VOCABULARY_DATABASE

def run_demo():
    """Run a demonstration of the Chinese learning app"""
    print("🇨🇳 中文学习应用演示")
    print("=" * 50)
    
    app = ChineseLearningApp()
    user_id = "demo_user"
    
    print("\n欢迎来到中文学习应用！")
    print("这个应用帮助用户通过造句练习学习中文词汇。")
    print("每个练习都会给用户一个词汇，用户需要用它造一个句子。")
    
    # Demo some example sessions
    demo_sentences = [
        "我们需要对这个产品进行多次迭代来改进用户体验。",
        "产品经理通过数据分析来了解用户需求。",
        "这家公司想要垄断整个市场。",
        "新功能将在下周上线。",
        "好的用户体验是产品成功的关键。"
    ]
    
    for i, demo_sentence in enumerate(demo_sentences, 1):
        print(f"\n" + "="*50)
        print(f"📚 练习 #{i}")
        
        # Start new session
        session = app.start_new_session(user_id)
        word = session["word"]
        
        print(f"词汇: {word['chinese']}")
        print(f"拼音: {word['pinyin']}")
        print(f"意思: {word['english']}")
        print(f"提示: {session['hint']}")
        
        # Simulate user input
        user_sentence = demo_sentence
        print(f"\n用户造句: {user_sentence}")
        
        # Process submission
        feedback = app.submit_sentence(user_id, user_sentence, word['chinese'])
        
        print(f"\n📝 反馈:")
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
    
    # Final summary
    final_progress = app.get_user_progress(user_id)
    print(f"\n" + "="*50)
    print(f"🎉 学习总结:")
    print(f"   总共学习了 {final_progress['words_learned']} 个词汇")
    print(f"   创造了 {final_progress['sentences_created']} 个句子")
    print(f"   完成了 {final_progress['total_sessions']} 次练习")
    print(f"   连续练习了 {final_progress['current_streak']} 次")
    
    if final_progress['recent_sentences']:
        print(f"\n📝 最近的句子:")
        for i, sentence_data in enumerate(final_progress['recent_sentences'], 1):
            print(f"   {i}. {sentence_data['word']}: {sentence_data['sentence']}")

def show_app_features():
    """Show the key features of the app"""
    print("\n🔧 应用功能特点:")
    print("=" * 50)
    
    features = [
        "📚 词汇数据库 - 包含中文、拼音、英文意思和例句",
        "🎯 个性化练习 - 随机选择词汇进行造句练习",
        "✅ 智能反馈 - 检查句子是否使用了指定词汇",
        "🏆 鼓励系统 - 提供积极的鼓励和赞美信息",
        "📖 示例句子 - 展示正确的用法和例句",
        "💡 使用提示 - 提供词汇使用的语法提示",
        "📊 进度跟踪 - 记录学习进度和连续练习次数",
        "🎨 多样化词汇 - 涵盖商业、技术等不同类别"
    ]
    
    for feature in features:
        print(f"   {feature}")
    
    print(f"\n📚 词汇库包含 {len(VOCABULARY_DATABASE)} 个词汇:")
    for word in VOCABULARY_DATABASE:
        print(f"   • {word.chinese} ({word.pinyin}) - {word.english}")

def show_workflow():
    """Show the app workflow"""
    print("\n🔄 应用工作流程:")
    print("=" * 50)
    
    workflow_steps = [
        "1. 用户启动应用",
        "2. 系统随机选择一个词汇",
        "3. 显示词汇的中文、拼音和英文意思",
        "4. 用户输入包含该词汇的句子",
        "5. 系统验证句子是否使用了指定词汇",
        "6. 提供反馈：成功/失败 + 鼓励信息",
        "7. 显示示例句子和使用提示",
        "8. 更新用户学习进度",
        "9. 询问是否继续练习",
        "10. 重复步骤2-9或结束学习"
    ]
    
    for step in workflow_steps:
        print(f"   {step}")

if __name__ == "__main__":
    print("选择演示内容:")
    print("1. 完整学习流程演示")
    print("2. 应用功能特点")
    print("3. 工作流程说明")
    
    choice = input("请输入选择 (1, 2, 或 3): ")
    
    if choice == "1":
        run_demo()
    elif choice == "2":
        show_app_features()
    elif choice == "3":
        show_workflow()
    else:
        print("运行完整演示...")
        run_demo() 