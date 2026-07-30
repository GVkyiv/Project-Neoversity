Overview
Whether or not you are a product manager with “AI” in your title, many PMs are increasingly expected to build features that incorporate AI in some way.

The fundamental skills needed to write an AI feature PRD are not that different from drafting a non-AI one:

You still need to define a problem well.
Ensure the solution addresses the problem.
Outline how you plan to mitigate risks.
However, an AI PRD needs to account for the fact that large language model (LLM) output is non-deterministic. How your user interacts with LLMs can lead to a wide range of outcomes. Choice of models and LLM techniques can impact results, sometimes dramatically. The rapid pace at which foundational models are evolving adds further complexities and opportunities. Managing the quality of your feature’s output and crafting a great user experience requires a solid grasp of how AI works.

By the end of this guide, you will be ready to draft a product spec for a generative AI feature that thoughtfully navigates the nuances and challenges of LLMs.

This guide, as well as the accompanying template, is intended for features that leverage generative AI as part of a broader user experience. This template is NOT intended for foundational models or general-purpose LLM chatbots.

What you'll do
Identify good use cases for AI: set the right groundwork.
Articulate the problem: make sure that you’re defining a real user problem.
Define the goal: articulate goals, non-goals, and success metrics.
Scope the solution: dive deep into user flows, AI-specific functionality requirements, and privacy and security considerations.
Align on technical considerations with engineering: collaborate with your engineering counterpart on technical LLM decisions.
Define the go-to-market plan: think beyond feature development to how you launch the feature.
Sign up to see more free resources

Create a free account to access artifacts, events, and more.

Become a member
Have an account? Log in

By creating an account, you agree to Reforge‘s Terms & Conditions

For more information, visit our FAQs.

1
Identify good use cases for AI

Good product management typically begins with identifying a user pain point (or opportunity for delight) and then developing a solution. AI product management can sometimes invert this process.

AI is often a hammer looking for a nail. Sometimes the product team is curious about generative AI and wants to explore ideas for how it can be applied. AI feature ideas can also arise when someone - sometimes a customer or executive - wants to inject AI into the product. While feature development ideally starts with identifying a user problem, the reality is that PMs may be handed a solution first and then asked to go back to evaluate if a worthwhile problem exists.

Make the most of this reality by finding good nails. Don’t make a hole somewhere else!

So how do you find a good nail?

Write_a_PRD_for_a_generative_AI_feature_1

Build a deep understanding of user needs
Start by taking a step back and asking questions about your product such as:

What are the main activities that a user does within my product? What are the broader problems that my product aims to solve?
What are the biggest user pain points? What is complex or tedious in the current flows?
What would delight users in a way that they didn’t even know they wanted?
Brainstorm how user needs can be improved via AI
Then consider how these user needs can be improved via AI. This way you stay rooted in the product’s core functions and purposes, as well as the known challenges. For example:

If the user has to consume a lot of content, would a summarization feature help?
If the user needs to write text that can be tedious to compose, would a content generation feature be helpful?
Think broadly about how these skills can be applied. LLMs can help you summarize a long PDF document, but they can also summarize a chat conversation, a phone call transcript, or a video. LLMs can help you generate paragraphs but also names, headings, replies, images, sound clips, even videos.

As a tip, this step does require you to have a baseline understanding what LLMs can currently do.

Common AI skills include summarization, question-answering, content generation, personalization, data processing, and predictive insights.

Here are some ways to deepen your understanding and intuition for what LLMs can do:

Try out foundational model LLM’s such as ChatGPT or Claude for a range of use cases. Understand their individual strengths and weaknesses.
Pay attention to how AI is being incorporated into the everyday apps you use. Where is it applied in novel, useful ways?
Work closely with your AI engineers to enhance your understanding. Participate in technical discussions. Review documentation related to the LLM techniques that your team is using. If you have AI feature ideas, ask them what would make them possible (or impossible) to build.
Determine which use cases are most valuable to your users
Among all the ways that AI can be applied to your product, which ones solve the biggest pain points and produce the most delight?

You can also consider which use cases differentiate your product most from competitors. What enables you to create “competitive moats” that can prevent competitors with a good model from duplicating your feature’s functionality? This could be the data available to train, the data used to generate the outputs, etc.

At this point, you are in more familiar territory. You are applying classic roadmap prioritization.

Finally, which user problems are best solved by AI as opposed to a different method?

Example

|

Zoom

Tip

|

Brainstorming ways to apply AI

2
Articulate the problem

When it comes to defining the problem in the PRD that your generative AI feature will solve, your problem statement shouldn’t even mention AI.

Your user’s problem is not that they lack AI in their lives!

Instead, focus on defining:

What is the user problem?
Why is it a problem?
How do you know it’s a problem?
To crystallize this, let’s consider an example of how a PM at Zoom might write the problem statement for an AI-enabled meeting summary feature. We’ll examine three scenarios: bad, good, and even better.

Write_a_PRD_for_a_generative_AI_feature_2

Bad example
Problem description: “Users don’t have an automated AI notetaker for all their meetings.”
Why this is bad: This states that the lack of the solution is the problem. It assumes that users need an AI notetaker. But why? It doesn’t describe the underlying problem or user goals. Asking “why” several times can help you get to a better problem statement.
Good example
Problem description: “Users want a record of the key points from their meetings, but it is tedious and distracting to take thorough manual notes for every meeting.”
Why it’s good: If you took this one at face value, you can imagine a range of solutions. You could, in the extreme, assign an intern to manually take notes for every meeting, or you could change the team’s process to force everyone to take collaborative notes. But an AI solution would be far more scalable and cost-effective.
Even better example
Problem description: “Users want a record of the discussion topics, key decisions, and action items from their meetings to follow through on the outcomes of a discussion, but it is tedious and distracting to take thorough manual notes for every meeting. In addition, users sometimes cannot attend a meeting, and they want a quick way to catch up on what they missed.”
Why it’s even better: It doesn’t just suggest that users want some record of the meeting. It suggests the kind of content that this record should focus on - key decisions and action items - and why. With the second use case, when users cannot attend a meeting, it suggests that the solution should have a way for users who cannot attend to request for notes. Lastly, it also suggests that the record should be easy and quick to consume.
3
Define the goals

When you have shipped your feature, what will users be able to accomplish? What outcomes will your feature produce for users?

To be clear, goals are not the same thing as your proposed solution. That comes later in the PRD.

When defining goals in your PRD, it’s important to outline goals, success metrics, and non-goals.

Write_a_PRD_for_a_generative_AI_feature_3

Goals
Consider, “What are the primary goals of your feature?”.

Your goals should tie back clearly to the problem statement.

Keep in mind that the goal isn’t for your user to use an AI feature. Describe the outcomes of your feature, regardless of whether it uses AI. You may decide that the problem you have identified is best solved without AI!

Non-goals
To clearly define the boundaries of your feature, state what is out of scope.

This can include feature ideas that are intended for future versions, long-standing problems that your feature will not solve, or adjacent issues that need to be addressed separately.

Success metrics
A common question is how goals are different than success metrics. Goals are a qualitative statement whereas success metrics are often numbers.

So think of success metrics as answering, “How will you know if your feature is successful?”.

Example metrics could measure DAU, MAU, clicks, key actions performed, tasks completed, retention, etc. Success metrics for AI features are generally similar to those for non-AI features. However, you may want additional metrics to measure quality. Keep in mind that measuring the quality of LLM output can be challenging as it is often subjective.

You may also want to evaluate the ultimate impact of your AI feature for your customers, as opposed to your company. As AI features often come packaged as costly add-ons, many customers want to evaluate their ROI.

What is the time saved, reduction in headcount, or quality improvement for customers because of the feature?

If you can’t find ideal ways to calculate these metrics, can you find good enough proxies instead? These considerations should be on your radar and you should be prepared to discuss them with customers.

Example

|

Zoom meeting summary feature

4
Scope the solution

Your solution should describe how the feature will work. Every AI feature will have different requirements, but there are three common attributes to describe: user flows, AI-specific requirements, and privacy considerations.

Write_a_PRD_for_a_generative_AI_feature_4

User flows
Describe how your feature will work. How will users interact with the feature? What steps are involved? What actions can the user take, and what outputs do they receive in return?

Describe the end-to-end user flow, which should include steps that both do and do not involve AI. Don’t just define the AI section and ignore the rest of the workflow that the user needs to complete the task.

For example, suppose you’re designing the user flow to detect scheduling intent from an email. Even if you can accurately detect when the user may want to schedule a meeting, you need to decide if your feature will automatically suggest available times of the sender, propose mutually available times if it has access to everyone’s calendars, or take the sender to a calendar app to complete the flow.

One key consideration is how to design the core interaction for users to invoke the LLM component. Common interactions for AI features:

Click a button: For example, summarize a chat thread.
One-shot prompt in a text field: For example, Notion for brainstorming ideas or Canva for generating a graphic for a social media post.
Pre-set prompts: For example, LinkedIn for takeaway questions that appear on posts.
Automated report: For example, Zoom meeting summaries if you have it set to auto-start or Slack daily recap of chats you missed.
Automated suggestions: For example, Superhuman 1-line email conversation summaries or Vanta suggested replies to a questionnaire.
Chatbot: For example, Intercom’s chatbot “Fin” answering customer support questions or Duolingo’s Roleplay for language learners to practice conversations.
A word of caution on chatbots. While chatbots have become the most obvious way to interact with an LLM, consider not starting with a chatbot.

It is harder to ensure the quality of responses, given that users can type literally anything into the text field. Users are more likely to struggle with a cold start problem. They may not know what to ask, how to phrase their requests, or how they can probe further in a conversation.

These issues can be mitigated with suggested use cases, suggested follow-up prompts, and different design patterns, but it is still worth exploring non-chatbot interactions first.

You may choose to mix and match these interactions or develop variations.

For example, Figjam assists you in creating a whiteboard template by providing pre-set prompt suggestions at each step, in addition to allowing the user to type free text into the prompt field. This saves the user from having to write an entire prompt from scratch and helps generate better-quality templates.

Another consideration is whether your AI feature’s workflow should have a human in the loop. If your feature might produce output that contains hallucinations or other inaccuracies that could lead to poor decisions or cause harm, consider adding a step where the user can review and edit (or delete) the content before it is shared more widely. For example, rather than have the LLM compose an email reply and send it immediately, have it prepare a draft, and let the user edit before sending.

AI-specific functionality requirements
This can be further broken down into multiple areas: user input + contextual data, LLM outputs, example prompts and LLM output, feedback mechanisms, and quality evaluation.

1. User input + contextual data: What input does the LLM need to consume?

User Input: How does the user invoke the LLM’s flow? Do they click buttons and type a prompt, or is it auto-generated when other events happen? For example:
Canva “Magic Switch”: user clicks the form factor that they want for their image
Notion question-answering: The user types a query
Gmail: The user clicks reply and a suggested reply is auto-generated
Contextual data: In addition to the user’s input, the LLM may need to consume additional data as the context from which to generate the response. It’s important to define the boundaries of this data, as large amounts of data or diverse sources of input may have different implications for the engineering solution. For example:
Notion: question-answering consumes the entire document
Loom: generates titles and chapters based on the transcript
Intercom: support chatbot consumes knowledge base articles
Microsoft 365 Copilot: consumes multiple data sources including the calendar, emails, documents, and contacts.
2. LLM output: What output does the LLM need to produce?

LLM output is necessarily non-deterministic. For many AI features, you cannot specify all the possible ways that the user will prompt the LLM, and you cannot predict how the LLM will respond. Nonetheless, you need to give guidance to your engineering team for the output you expect.
Describe general requirements and principles for your expected output, independent of any examples. For example, define the length, tone, and format of the response. Describe what the content should focus on or exclude.
Your examples should demonstrate what good looks like. Pick a good range of examples:
Common cases that many users will try.
Key cases that are critical to get right.
A few obscure examples to show the boundaries of what your feature can or cannot do.
Categorize your use cases if there are several different types. For example, a chatbot that needs to both summarize and perform question-answering.
As a tip, you may want to prototype answers using an LLM like ChatGPT or Claude. For example, it’s difficult to manually write a meeting summary. However, you can upload a transcript to ChatGPT and prompt it to generate a summary. You can also try this with actions like generating slides using AI slide deck generation apps in the market, and then modifying the output to describe what you want.
3. Feedback mechanisms: How will users give feedback to improve quality?

Even the best QA plan cannot anticipate how your product will be used in the wild. To monitor and improve quality, consider adding feedback mechanisms for your users. Some examples to consider:
Thumbs up / down. The pro is that this is lightweight and will have higher response rates from users. The con is that this lacks detail on why a user thought the feature’s output was good or bad.
Feedback form that includes scoring and/or open text fields. Specify what additional data from the LLM interaction (user input + model output) will be shared with the company as part of the feedback. The pro here is that the user has the opportunity to explain what exactly they didn’t like. The tradeoff is potentially lower response rates as more effort is required of users.
4. Quality evaluation: How do you know when the feature is ready for launch?

LLM quality will never be perfect, and it can also be challenging to quantify. What would convince you that the product is ready for launch? What would convince your stakeholders that it is ready?
The quality bar may shift depending on how the LLM output is consumed by the user:
Examples of higher risk tolerance:
Is there a human in the loop to check quality before the output is published? For example, the LLM drafts an answer, but the human edits before sending.
Does the output save significant time and therefore even 50% accuracy is valuable?
Examples of lower risk tolerance:
Can inaccuracies lead to poor decisions or even cause harm?
Can the long tail produce potentially highly offensive output?
You should consider how to do both automatic and manual evaluations.
Automated evaluations: Work with your engineering team to set up an automated process, which often involves other LLMs, to evaluate LLM output. Create a data set of examples for your feature. The process should run the feature’s tasks on your data set, and then automatically score the output based on criteria you have defined.
Manual evaluations: Regardless of automated testing, you as PM, your QA team, and/or a group of testers should also perform manual testing to assess the quality of the output and catch nuances that automated evaluations cannot capture.
You are looking for convergence between your automated and manual evaluation metrics. You may find that anecdotal data on a small sample is a reasonable indicator of overall quality. Your small manual sample will not catch issues in the long tail, but as you iterate with engineering on the model, anecdotal data may be a good shortcut to help you gauge whether quality is improving.
If quality is not up to par, work with your engineering team to try ways to improve:
Experiment with prompt engineering and/or retrieval augmented generation (RAG)
Scrub the underlying data set
Source additional or different data sets to fine-tune the model
Try other foundational models
Privacy, security, and ethical considerations
Three important aspects to consider are security and privacy, settings and controls, and safeguards for responsible AI.

1. Security and privacy: Conventions and industry standards are starting to form around what disclosures, consents, and controls are expected of AI products. But ultimately, users themselves want to know when AI is running and how their data is being handled. Work with your legal team to establish what is necessary, appropriate, and helpful to disclose to users.

Actions that may require disclosures
AI is running or AI was applied.
AI can be wrong in these ways.
AI was used to generate the content.
Your data will be processed by AI in these ways.
Actions that may require consent
Your data is/is not being used to train models.
Your data will be retained in these ways (E.g. a recording or transcript is retained).
2. Settings and controls: To give users more assurance about how your AI feature works, you may wish to consider:

Is the feature default on or off?
Do users need a “kill switch” to stop the feature?
How can users remove any sensitive data from the feature’s data sources?
Can users opt in or opt out of allowing their data to be used for model training?
What is the default data retention period and can it be customized?
3. Safeguards for responsible AI: Anticipate how your product may be abused. Consider how it may generate offensive content even when used correctly. Check for biases in the output and plan mitigation strategies.

You may decide to apply content moderation filters on the user’s input or the model’s output. You may decide to change the feature’s design to limit abuse (e.g. instead of a free text field, the user can only select from a few options). You may not be able to eliminate egregious outcomes entirely.
Discuss with your legal team, trust & safety team, and other internal stakeholders how you plan to assess the risks, mitigate them, and align on a risk threshold.
For example, an image generation feature may produce images of humans that carry racial or gender bias. Should this issue be mitigated with warnings, modifications to abstract the humans, modifications to remove the humans, etc.?
Example

|

Zoom meeting summary feature

5
Align on technical considerations with engineering

Technical considerations are especially important in an AI feature PRD.

While these technical considerations are typically driven by your engineering counterpart, it is crucial for the PM to understand the key technologies and collaborate with engineering on the technical decisions that have product and user implications.

Some of the key components you’ll want to define include:

Write_a_PRD_for_a_generative_AI_feature_5

Prompting the LLM
Depending on your company and the actual feature, the PM may or may not be responsible for writing the actual prompt that is sent to the LLM.

In some cases, the user’s prompt is sent directly to the LLM. In other cases, the user’s input prompt may be incorporated into a larger prompt crafted by your team.

Model selection
Model selection is typically led by the engineering team. The PM may be called to give input on the use of 1st vs. 3rd party models, data privacy requirements, nature of training data, and scaling requirements.

LLM techniques
Your engineering team will typically lead the decisions on whether your feature is best delivered by fine-tuning a model, applying retrieval augmented generation (RAG), or other LLM techniques. These options are constantly evolving and improving!

Understanding how these techniques work will help you work more collaboratively with the engineers and design your feature to make the most of these technologies.

Scaling needs
GPUs (graphics processing units) are expensive and can require effort to obtain. Work with your data science and engineering teams to estimate potential usage and capacity needed. Consider if your feature has particular needs, such as international deployment or special data residency requirements, and raise these early with your infrastructure team.

Tip

|

Don’t over-spec

6
Define the go-to-market plan

It’s important to consider how you plan to bring your AI feature to market given that GPUs are expensive.

When defining your GTM plan, make sure to consider:

Write_a_PRD_for_a_generative_AI_feature_6

How will you roll out the feature to users in a way that mitigates risk?
How you will price the feature with respect to the rest of the product?
How you will enable cross-functional teams like sales and customer success?
Rollout plan
Even with significant testing by the product team of an AI feature before launch, the LLM output remains non-deterministic. To monitor quality across a wider range of use cases, consider starting your feature rollout with a beta program.

This gives you a chance to receive feedback and iterate on quality and design before opening the floodgates. Depending on the risks and urgency of completing the rollout, you may consider setting up successive tiers:

Write_a_PRD_for_a_generative_AI_feature_7

Enable for any internal user to test
Invite several early-adopter customers to test
Open up the beta to select tiers of customers
Generally available
Pricing
Many companies have packaged their AI features as an add-on, due to the cost of providing LLM-powered features and the market’s willingness to pay.

As you roll out your feature, consider your pricing options:

Will your feature be priced as a new add-on SKU?
Will it be part of an existing AI add-on package or included in an existing premium tier?
Will it be offered for free to all paying users?
Will it be part of a free trial to encourage users to upgrade to a premium tier?
Cross-functional enablement
It’s important to arm your sales and customer success teams with materials on how to pitch your features to customers.

Describe how your AI feature fits within the company’s broader AI narrative.
Pay special attention to privacy and security issues, as these are often top of mind for B2B customers.
Additionally, consider preparing an FAQ or creating an internal chat channel where field teams can get answers to their questions.

Example

|

Zoom meeting summary

Recap

Identify good use cases for AI: Begin by understanding user needs before brainstorming AI applications and evaluating those applications. Prioritize the use cases that solve meaningful pain points for users and create differentiation from competitors.
Define the problem: The problem statement should focus on the user issue, not the lack of AI. Clearly describe the problem, why it is an issue, and how you know it's a problem.
Define the goals: Outline goals, non-goals, and success metrics. Goals are qualitative feature outcomes, non-goals are what is out of scope, and success metrics are qualitative targets.
Scope the solution: Like other PRDs, detail the end-to-end user flow, including interactions with and without AI. What’s unique for AI feature PRDs is adding more detail on AI-specific functionality requirements and privacy and security considerations.
AI-specific requirements: Define the user input, contextual data, LLM output, feedback mechanisms, and quality evaluation methods.
Privacy and security concerns: Address security, privacy, settings, and controls. Ensure ethical considerations are accounted for to prevent misuse and bias.
Align on technical considerations with engineering: Make sure to partner with your engineering counterparts on decisions like prompt engineering, model selection, LLM techniques, and scaling needs. PMs should understand these technical components and be able to weigh in on these decisions.
Define the go-to-market plan: Think beyond feature development to how to launch the feature, including the roll-out plan, pricing, and cross-functional enablement.