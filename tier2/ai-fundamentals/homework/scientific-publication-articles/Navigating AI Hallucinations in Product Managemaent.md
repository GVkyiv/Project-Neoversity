Navigating AI Hallucinations in Product Management
As I continue my journey into AI, one of the most fascinating—and frustrating—aspects is understanding how Large Language Models (LLMs) work, and more importantly, where they break.

In a recent post, I shared my personal goal: to digitally transform Product Management at RapidScale This means offloading some of the more mundane PM tasks that shouldn't exist in 2025. If you search “What Product Management tasks can AI perform?” you’ll see examples like:

🔍 Deep customer insights & market research
📊 Forecasting & roadmap planning
🧠 Predicting user behavior
🛠️ Automating repetitive tasks
📈 Performance monitoring
🥊 Competitive analysis

I’ve already started building tools to tackle some of these, especially competitive analysis. But I’ve hit a wall—data hallucinations.

What Are AI Hallucinations?
In short: when an AI model generates false, nonsensical, or exaggerated information. And yes, they’re very real.

Why do they happen? It varies, but common causes include:

Outdated, low-quality, or biased training data
Lack of domain context or clarity in instructions
Model overfitting or poor prompt engineering

A simple comparison:

Unsupervised Learning (e.g., ChatGPT prompt) = more hallucinations
Supervised Learning (e.g., code that analyzes structured data) = more control
Hybrid (my use case) = tricky middle ground

My Use Case: Competitive Analysis Tool
I’m building a tool that:

Takes a few parameters (see image below 👇)
Scrapes websites and analyst sources (robots.txt respected)
Sends the data to an LLM for synthesis

Article content
But... here’s where hallucinations sneak in. I’ve seen:

❌ Overstated claims about companies
❌ Misrepresented services or market position

In most cases, the LLM isn’t lying maliciously—it’s interpreting data with poor or missing context.

How I’m Fixing It 🛠️
1. Improve prompt clarity Bad: “Compare Company A vs. B” Better: “As a Product Manager at Company A, I need a competitive analysis on X, Y, and Z with focus on gaps, future trends, and value prop differentiation.”

2. Review scraped data manually Before trusting what the LLM produces, I’m verifying that the source data is meaningful. If it's garbage in, it's garbage out.

3. Decide how to refine: manual vs. automated Right now, my refinement process is manual. But I’m exploring:

🔁 Prompt Engineering
🔗 Chain-of-thought prompting
🧠 Retrieval-Augmented Generation (RAG)
🧬 Reinforcement Learning with Human Feedback (RLHF)

Final Thoughts
This journey has made one thing clear: context is king. The more you define your role, audience, and goal for the model, the fewer hallucinations you'll face. As AI becomes a core part of product management, knowing how to guide it becomes just as critical as knowing how to use it.

If you’re building similar tools or tackling AI in your PM org, I’d love to connect and swap notes.