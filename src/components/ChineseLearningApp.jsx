import React, { useState, useEffect, useCallback } from 'react';
import './ChineseLearningApp.css';

// Mock data - in a real app, this would come from the backend
const VOCABULARY_DATA = [
  {
    chinese: "数据分析",
    pinyin: "shù jù fēn xī",
    english: "Data analysis",
    example_sentence: "产品经理需要通过数据分析来了解用户行为并优化功能。",
    category: "business"
  },
  {
    chinese: "迭代",
    pinyin: "dié dài",
    english: "Iteration",
    example_sentence: "为了提升用户体验，我们计划对这个功能进行多次迭代。",
    category: "business"
  },
  {
    chinese: "产品经理",
    pinyin: "chǎn pǐn jīng lǐ",
    english: "Product Manager",
    example_sentence: "我们的产品经理负责制定产品战略并协调各个部门的工作。",
    category: "business"
  },
  {
    chinese: "垄断",
    pinyin: "lǒng duàn",
    english: "Monopoly",
    example_sentence: "虾贝想要垄断电商市场。",
    category: "business"
  },
  {
    chinese: "上线",
    pinyin: "shàng xiàn",
    english: "Go live / Launch (a feature or product)",
    example_sentence: "我们计划下周一将新功能上线。",
    category: "business"
  },
  {
    chinese: "用户体验",
    pinyin: "yòng hù tǐ yàn",
    english: "User experience",
    example_sentence: "好的用户体验是产品成功的关键。",
    category: "business"
  },
  {
    chinese: "优化",
    pinyin: "yōu huà",
    english: "Optimize",
    example_sentence: "我们需要优化这个功能以提高效率。",
    category: "business"
  },
  {
    chinese: "功能",
    pinyin: "gōng néng",
    english: "Feature / Function",
    example_sentence: "这个新功能很受用户欢迎。",
    category: "business"
  },
  {
    chinese: "市场",
    pinyin: "shì chǎng",
    english: "Market",
    example_sentence: "我们需要分析市场趋势来制定策略。",
    category: "business"
  },
  {
    chinese: "策略",
    pinyin: "cè lüè",
    english: "Strategy",
    example_sentence: "公司制定了新的营销策略。",
    category: "business"
  }
];

const PRAISE_MESSAGES = [
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
];

const ENCOURAGEMENT_MESSAGES = [
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
];

const USAGE_TIPS = {
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
};

function ChineseLearningApp() {
  const [currentWord, setCurrentWord] = useState(null);
  const [userSentence, setUserSentence] = useState('');
  const [feedback, setFeedback] = useState(null);
  const [showFeedback, setShowFeedback] = useState(false);
  const [progress, setProgress] = useState({
    wordsLearned: 0,
    sentencesCreated: 0,
    currentStreak: 0,
    totalSessions: 0
  });
  const [usedWords, setUsedWords] = useState([]);
  const [recentSentences, setRecentSentences] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  // Get a random word that hasn't been used recently
  const getRandomWord = useCallback(() => {
    const availableWords = VOCABULARY_DATA.filter(word => 
      !usedWords.includes(word.chinese)
    );
    
    if (availableWords.length === 0) {
      setUsedWords([]);
      return VOCABULARY_DATA[Math.floor(Math.random() * VOCABULARY_DATA.length)];
    }
    
    return availableWords[Math.floor(Math.random() * availableWords.length)];
  }, [usedWords]);

  // Start a new session
  const startNewSession = useCallback(() => {
    const word = getRandomWord();
    setCurrentWord(word);
    setUserSentence('');
    setFeedback(null);
    setShowFeedback(false);
    setIsLoading(false);
  }, [getRandomWord]);

  // Submit sentence and get feedback
  const submitSentence = () => {
    if (!userSentence.trim()) {
      setFeedback({
        success: false,
        message: "请写一个句子！",
        example_sentence: currentWord.example_sentence,
        encouragement: ENCOURAGEMENT_MESSAGES[Math.floor(Math.random() * ENCOURAGEMENT_MESSAGES.length)]
      });
      setShowFeedback(true);
      return;
    }

    if (!userSentence.includes(currentWord.chinese)) {
      setFeedback({
        success: false,
        message: `请在你的句子中使用词汇 '${currentWord.chinese}'！`,
        example_sentence: currentWord.example_sentence,
        encouragement: ENCOURAGEMENT_MESSAGES[Math.floor(Math.random() * ENCOURAGEMENT_MESSAGES.length)]
      });
      setShowFeedback(true);
      return;
    }

    // Success case
    const praise = PRAISE_MESSAGES[Math.floor(Math.random() * PRAISE_MESSAGES.length)];
    const encouragement = ENCOURAGEMENT_MESSAGES[Math.floor(Math.random() * ENCOURAGEMENT_MESSAGES.length)];
    
    setFeedback({
      success: true,
      message: praise,
      user_sentence: userSentence,
      example_sentence: currentWord.example_sentence,
      word_analysis: {
        chinese: currentWord.chinese,
        pinyin: currentWord.pinyin,
        english: currentWord.english,
        usage_tip: USAGE_TIPS[currentWord.chinese] || "这个词汇可以根据语境灵活使用。"
      },
      encouragement: encouragement
    });

    // Update progress
    setProgress(prev => ({
      wordsLearned: prev.wordsLearned + (usedWords.includes(currentWord.chinese) ? 0 : 1),
      sentencesCreated: prev.sentencesCreated + 1,
      currentStreak: prev.currentStreak + 1,
      totalSessions: prev.totalSessions + 1
    }));

    // Add to used words
    setUsedWords(prev => [...prev, currentWord.chinese]);

    // Add to recent sentences
    setRecentSentences(prev => [...prev, {
      word: currentWord.chinese,
      sentence: userSentence,
      timestamp: new Date().toISOString()
    }]);

    setShowFeedback(true);
  };

  // Start first session on component mount
  useEffect(() => {
    startNewSession();
  }, [startNewSession]);

  return (
    <div className="chinese-learning-app">
      <header className="app-header">
        <h1>🇨🇳 中文学习应用</h1>
        <p>通过造句练习学习中文词汇</p>
      </header>

      <div className="app-container">
        {/* Progress Bar */}
        <div className="progress-section">
          <div className="progress-stats">
            <div className="stat">
              <span className="stat-number">{progress.wordsLearned}</span>
              <span className="stat-label">已学词汇</span>
            </div>
            <div className="stat">
              <span className="stat-number">{progress.sentencesCreated}</span>
              <span className="stat-label">造句数量</span>
            </div>
            <div className="stat">
              <span className="stat-number">{progress.currentStreak}</span>
              <span className="stat-label">连续练习</span>
            </div>
          </div>
        </div>

        {/* Main Learning Section */}
        <div className="learning-section">
          {currentWord && (
            <div className="word-card">
              <div className="word-header">
                <h2 className="chinese-word">{currentWord.chinese}</h2>
                <p className="pinyin">{currentWord.pinyin}</p>
                <p className="english-meaning">{currentWord.english}</p>
              </div>

              <div className="instruction">
                <p>请使用上面的词汇造一个句子：</p>
              </div>

              <div className="sentence-input">
                <textarea
                  value={userSentence}
                  onChange={(e) => setUserSentence(e.target.value)}
                  placeholder="在这里输入你的句子..."
                  className="sentence-textarea"
                  rows="3"
                />
              </div>

              <div className="action-buttons">
                <button 
                  className="submit-btn"
                  onClick={submitSentence}
                  disabled={isLoading}
                >
                  {isLoading ? '提交中...' : '提交句子'}
                </button>
                <button 
                  className="new-word-btn"
                  onClick={startNewSession}
                >
                  下一个词汇
                </button>
              </div>
            </div>
          )}

          {/* Feedback Section */}
          {showFeedback && feedback && (
            <div className={`feedback-card ${feedback.success ? 'success' : 'error'}`}>
              <div className="feedback-header">
                <span className="feedback-icon">
                  {feedback.success ? '✅' : '❌'}
                </span>
                <h3>{feedback.message}</h3>
              </div>

              <div className="feedback-content">
                <div className="example-section">
                  <h4>📖 示例句子</h4>
                  <p className="example-sentence">{feedback.example_sentence}</p>
                </div>

                {feedback.success && feedback.word_analysis && (
                  <div className="usage-tip-section">
                    <h4>💡 使用提示</h4>
                    <p className="usage-tip">{feedback.word_analysis.usage_tip}</p>
                  </div>
                )}

                <div className="encouragement-section">
                  <p className="encouragement">{feedback.encouragement}</p>
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Recent Sentences */}
        {recentSentences.length > 0 && (
          <div className="recent-sentences">
            <h3>📝 最近的句子</h3>
            <div className="sentences-list">
              {recentSentences.slice(-3).map((sentenceData, index) => (
                <div key={index} className="sentence-item">
                  <span className="sentence-word">{sentenceData.word}</span>
                  <span className="sentence-text">{sentenceData.sentence}</span>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default ChineseLearningApp; 