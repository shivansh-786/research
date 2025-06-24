#!/usr/bin/env python3
"""
Prompt Templates for Zeron Research Agent
Contains specialized prompts for different types of queries and responses
"""

class PromptTemplates:
    """Collection of prompt templates for the research agent"""
    
    @staticmethod
    def get_classification_prompt():
        """Dynamic classification prompt that adapts based on context"""
        return """
        You are an intelligent query router for Zeron's research system. Your job is to determine the optimal search strategy.

        ZERON'S CAPABILITIES:
        - Compliance management platform
        - Attack surface management tools
        - Cyber risk management solutions
        - Vendor management system
        - Integration capabilities and APIs

        QUERY TO ANALYZE: "{query}"

        CONTEXT FROM QUICK RAG CHECK:
        {rag_context}

        CLASSIFICATION LOGIC:

        🏠 CHOOSE "RAG Only" WHEN:
        - Query asks about Zeron's specific features, capabilities, or processes
        - Technical documentation or how-to questions about Zeron products
        - Integration guides, API documentation, or internal workflows
        - Configuration, setup, or troubleshooting for Zeron systems
        - Questions that can be fully answered from internal documentation

        🌐 CHOOSE "RAG + Web Search" WHEN:
        - Competitive analysis or comparisons with other vendors
        - Market research, industry trends, or benchmarking
        - Battle card creation or competitive positioning
        - Questions about external products, vendors, or solutions
        - Pricing comparisons or market analysis
        - "Top competitors", "market leaders", "industry standards"
        - Queries mentioning specific competitor names or external tools
        - Questions that benefit from current market intelligence

        🎯 SPECIAL INDICATORS:
        - Words like "vs", "compared to", "battle card", "competitors" → Web Search
        - External company/product names → Web Search  
        - "Latest trends", "market size", "industry analysis" → Web Search
        - "How does [Zeron product] work" → RAG Only
        - "What is [Zeron feature]" → RAG Only

        RESPOND WITH JSON:
        {{
            "requires_web_search": true/false,
            "search_strategy": "RAG Only" or "RAG + Web Search",
            "reasoning": "Specific explanation for the decision",
            "confidence": "high/medium/low"
        }}
        """
    
    @staticmethod
    def get_battle_card_template():
        """Enhanced template for competitive battle cards with clear difference highlighting"""
        return """
        Create a comprehensive BATTLE CARD that clearly highlights differences between Zeron and competitors.

        USER REQUEST: {query}

        ZERON'S INTERNAL CONTEXT:
        {internal_context}

        COMPETITIVE INTELLIGENCE:
        {external_research}

        BATTLE CARD STRUCTURE:

        # 🎯 COMPETITIVE BATTLE CARD: {comparison_title}

        ## 📊 EXECUTIVE SUMMARY & WIN/LOSS ASSESSMENT
        
        ### 🏆 ZERON'S COMPETITIVE POSITION
        - **Overall Market Advantage**: [High/Medium/Low] - [Why]
        - **Key Differentiating Factors**: [Top 3 unique advantages]
        - **Recommended Win Strategy**: [Primary approach for this competitor]
        - **Win Probability**: [High/Medium/Low] - [In what scenarios]

        ### ⚡ QUICK DIFFERENTIATION SUMMARY
        | **What Makes Zeron Different** | **Impact on Customer** |
        |--------------------------------|------------------------|
        | [Key Differentiator #1] | [Specific customer benefit] |
        | [Key Differentiator #2] | [Specific customer benefit] |
        | [Key Differentiator #3] | [Specific customer benefit] |

        ## 🥊 DETAILED COMPETITIVE COMPARISON

        ### 🟢 AREAS WHERE ZERON WINS
        
        | **Capability** | **🏆 Zeron** | **🔴 {competitor_name}** | **🎯 Why Zeron Wins** | **💬 Sales Message** |
        |----------------|---------------|--------------------------|------------------------|-------------------|
        | **[Feature 1]** | ✅ [Zeron's approach] | ❌ [Competitor limitation] | [Specific advantage] | "[Elevator pitch]" |
        | **[Feature 2]** | ✅ [Zeron's approach] | ⚠️ [Competitor weakness] | [Specific advantage] | "[Elevator pitch]" |
        | **[Feature 3]** | ✅ [Zeron's approach] | ❌ [Competitor gap] | [Specific advantage] | "[Elevator pitch]" |

        ### 🟡 COMPETITIVE PARITY AREAS
        
        | **Capability** | **Zeron** | **{competitor_name}** | **Differentiation Strategy** |
        |----------------|-----------|----------------------|------------------------------|
        | **[Feature A]** | [Zeron capability] | [Similar capability] | [How to position differently] |
        | **[Feature B]** | [Zeron capability] | [Similar capability] | [How to position differently] |

        ### 🔴 AREAS OF COMPETITIVE CHALLENGE
        
        | **Area** | **⚠️ Challenge** | **🛡️ Defense Strategy** | **🔄 Redirect Message** |
        |----------|------------------|------------------------|------------------------|
        | **[Area 1]** | [What they do better] | [How to defend] | [How to redirect conversation] |
        | **[Area 2]** | [Their advantage] | [Counter-positioning] | [Alternative value proposition] |

        ## 🏢 COMPANY & SOLUTION COMPARISON

        ### 📈 ZERON ADVANTAGES
        ```
        🎯 FOCUS AREA: [Zeron's specialization]
        📊 MARKET POSITION: [How Zeron is positioned differently]
        🔧 TECHNICAL APPROACH: [Unique technical differentiators]
        👥 CUSTOMER BASE: [Target customer differences]
        🚀 INNOVATION: [Latest capabilities competitors lack]
        ```

        ### 📉 COMPETITOR PROFILE: {competitor_name}
        ```
        🎯 FOCUS AREA: [Their main focus]
        📊 MARKET POSITION: [How they position themselves]
        ⚠️ LIMITATIONS: [Key weaknesses to exploit]
        💰 PRICING MODEL: [How their pricing differs]
        📅 RECENT MOVES: [Latest developments]
        ```

        ## 💰 PRICING & VALUE COMPARISON

        ### 💎 ZERON'S VALUE PROPOSITION
        | **Pricing Factor** | **Zeron Advantage** | **Competitive Difference** |
        |-------------------|---------------------|---------------------------|
        | **Cost Model** | [Zeron's approach] | [How it's better than competitor] |
        | **ROI Timeline** | [Zeron's ROI] | [Faster/better than competitor] |
        | **Hidden Costs** | [Zeron transparency] | [Competitor hidden costs] |
        | **Scalability** | [Zeron scaling] | [Competitor scaling issues] |

        ### 🎯 VALUE-BASED SELLING POINTS
        - **"Unlike {competitor_name}, Zeron offers..."** [Key differentiator]
        - **"While {competitor_name} requires [X], Zeron provides..."** [Advantage]
        - **"Where {competitor_name} falls short in [Y], Zeron excels by..."** [Superiority]

        ## 🗣️ SALES CONVERSATION TOOLKIT

        ### 🎪 OPENING DIFFERENTIATORS (First 30 seconds)
        1. **"What makes us different from {competitor_name} is..."** [Primary differentiator]
        2. **"Unlike {competitor_name}, we specialize in..."** [Unique focus]
        3. **"Where {competitor_name} struggles with [X], we excel because..."** [Advantage]

        ### 🛡️ OBJECTION HANDLING SCRIPTS
        | **Objection** | **🔄 Immediate Response** | **✅ Follow-up Proof** |
        |---------------|--------------------------|----------------------|
        | **"{competitor_name} has more features"** | "More features often mean complexity. Here's what matters..." | [Specific customer example] |
        | **"{competitor_name} is cheaper"** | "Let's look at total cost of ownership..." | [ROI comparison] |
        | **"{competitor_name} is more established"** | "Established can mean legacy. Here's why newer is better..." | [Innovation examples] |

        ### 🔍 DISCOVERY QUESTIONS TO WIN
        - **"What challenges have you had with [competitor capability]?"** *(Uncover their weaknesses)*
        - **"How important is [Zeron strength] to your organization?"** *(Highlight our advantages)*
        - **"What would happen if [competitor limitation] became a problem?"** *(Create urgency)*

        ## 📊 COMPETITIVE POSITIONING MATRIX

        ```
        FEATURE COMPARISON SCORECARD:
        
        ✅ = Clear Advantage  ⚠️ = Competitive  ❌ = Disadvantage
        
        | Feature Category | Zeron | {competitor_name} | Winner |
        |-----------------|-------|------------------|--------|
        | Core Platform   | ✅    | ⚠️               | Zeron  |
        | Integration     | ✅    | ❌               | Zeron  |
        | User Experience| ✅    | ⚠️               | Zeron  |
        | Scalability     | ✅    | ❌               | Zeron  |
        | Support         | ✅    | ⚠️               | Zeron  |
        | Pricing         | ✅    | ❌               | Zeron  |
        ```

        ## 🏆 WIN STRATEGY & TACTICS

        ### 🎯 IDEAL COMPETITIVE SCENARIO
        - **Customer Profile**: [When to compete aggressively]
        - **Use Cases**: [Where Zeron has strongest advantage]
        - **Decision Criteria**: [What factors favor Zeron]

        ### 📈 PROOF POINTS & AMMUNITION
        - **Customer Success Stories**: [Specific wins against this competitor]
        - **Technical Benchmarks**: [Performance comparisons]
        - **ROI Evidence**: [Quantified benefits over competitor]
        - **Industry Recognition**: [Awards, certifications Zeron has that competitor lacks]

        ### 🚫 WHEN NOT TO COMPETE
        - **Avoid if**: [Scenarios where competitor might win]
        - **Alternative Strategy**: [How to reposition or redirect]

        ## 📰 RECENT COMPETITIVE INTELLIGENCE

        ### 🆕 LATEST DEVELOPMENTS
        - **Zeron Recent Wins**: [Latest capabilities/announcements]
        - **{competitor_name} Recent Moves**: [Their latest developments]
        - **Market Shifts**: [Trends that favor Zeron]

        ### 🔮 FUTURE OUTLOOK
        - **Zeron Roadmap Advantages**: [Upcoming capabilities]
        - **Competitive Threats**: [What to watch for]
        - **Market Opportunities**: [Trends favoring Zeron]

        ---
        **🎯 BATTLE CARD QUICK REFERENCE:**
        - **Primary Message**: [One-liner differentiator]
        - **Backup Messages**: [2-3 alternative angles]
        - **Proof Point**: [Strongest evidence]
        - **Next Action**: [Recommended next step in sales process]

        *Generated: {timestamp} | Confidence: [High/Medium/Low] | Last Updated: [Date]*
        """
    
    @staticmethod
    def get_market_analysis_template():
        """Template for market research and industry analysis"""
        return """
        Provide comprehensive market analysis combining Zeron's position with industry intelligence.

        QUERY: {query}

        ZERON'S CONTEXT:
        {internal_context}

        MARKET RESEARCH:
        {external_research}

        ANALYSIS STRUCTURE:

        # 📊 MARKET ANALYSIS: {analysis_title}

        ## 🔍 EXECUTIVE SUMMARY
        - Key market trends affecting Zeron's business
        - Strategic implications and opportunities
        - Recommended actions

        ## 🌐 MARKET LANDSCAPE
        
        ### Market Size & Growth
        - Current market valuation and growth projections
        - Key growth drivers and market dynamics
        - Geographic and segment breakdown

        ### Key Players & Positioning
        - Market leaders and their positioning
        - Emerging players and disruptors
        - Zeron's current market position

        ## 🎯 ZERON'S MARKET POSITION

        ### Strengths in Current Market
        - How Zeron's capabilities align with market needs
        - Competitive advantages in key segments
        - Customer validation and market traction

        ### Market Opportunities
        - Underserved segments or use cases
        - Emerging trends that favor Zeron's approach
        - Partnership or expansion opportunities

        ### Market Challenges
        - Competitive pressures and market shifts
        - Technology or regulatory changes
        - Resource or capability gaps

        ## 📈 STRATEGIC RECOMMENDATIONS
        
        ### Short-term (3-6 months)
        - Immediate market opportunities to pursue
        - Competitive responses needed
        - Marketing and positioning adjustments

        ### Medium-term (6-18 months)
        - Product development priorities based on market needs
        - Market expansion or segment targeting
        - Partnership or acquisition considerations

        ## 🔮 MARKET OUTLOOK
        - Future market evolution and trends
        - Potential disruptions or changes
        - Long-term positioning strategy for Zeron
        """
    
    @staticmethod
    def get_technical_comparison_template():
        """Template for technical feature comparisons"""
        return """
        Create a detailed technical comparison focusing on capabilities and implementation.

        REQUEST: {query}

        ZERON TECHNICAL CONTEXT:
        {internal_context}

        EXTERNAL TECHNICAL RESEARCH:
        {external_research}

        # 🔧 TECHNICAL COMPARISON: {comparison_title}

        ## 📋 CAPABILITY MATRIX

        | Capability | Zeron | {competitor_name} | Technical Advantage |
        |------------|-------|------------------|-------------------|
        | **Architecture** | [Zeron's approach] | [Competitor's approach] | [Analysis] |
        | **Integration** | [Zeron's methods] | [Competitor's methods] | [Analysis] |
        | **Scalability** | [Zeron's approach] | [Competitor's approach] | [Analysis] |
        | **Security** | [Zeron's features] | [Competitor's features] | [Analysis] |
        | **APIs** | [Zeron's API capabilities] | [Competitor's API] | [Analysis] |

        ## 🏗️ ARCHITECTURE COMPARISON
        
        ### Zeron's Technical Approach
        - System architecture and design principles
        - Technology stack and implementation details
        - Scalability and performance characteristics

        ### {competitor_name}'s Technical Approach
        - Their architecture and technology choices
        - Implementation methodology
        - Known technical limitations or strengths

        ## ⚡ PERFORMANCE & SCALABILITY
        - Benchmark comparisons (if available)
        - Scalability limits and performance metrics
        - Real-world deployment considerations

        ## 🔌 INTEGRATION CAPABILITIES
        - Native integrations and partnerships
        - API flexibility and developer experience
        - Custom integration complexity

        ## 🛡️ SECURITY & COMPLIANCE
        - Security frameworks and certifications
        - Compliance standard support
        - Data handling and privacy features

        ## 🎯 TECHNICAL DECISION FACTORS
        - When to recommend Zeron over competitors
        - Technical evaluation criteria for prospects
        - Proof-of-concept recommendations
        """
    
    @staticmethod
    def get_synthesis_prompt(query_type: str):
        """Get appropriate synthesis prompt based on query type"""
        if any(keyword in query_type.lower() for keyword in ['battle', 'vs', 'compared', 'competitor']):
            return PromptTemplates.get_battle_card_template()
        elif any(keyword in query_type.lower() for keyword in ['market', 'industry', 'trend', 'analysis']):
            return PromptTemplates.get_market_analysis_template()
        elif any(keyword in query_type.lower() for keyword in ['technical', 'architecture', 'feature']):
            return PromptTemplates.get_technical_comparison_template()
        else:
            return PromptTemplates.get_general_synthesis_template()
    
    @staticmethod
    def get_general_synthesis_template():
        """General synthesis template for mixed queries"""
        return """
        Create a comprehensive response that expertly combines internal knowledge with external research.

        USER QUERY: {query}

        ZERON'S INTERNAL KNOWLEDGE:
        {internal_context}

        EXTERNAL RESEARCH:
        {external_research}

        SYNTHESIS INSTRUCTIONS:

        1. **Lead with Zeron's Perspective**: Start with how Zeron addresses the query topic
        
        2. **Integrate Market Context**: Add relevant external insights and industry context
        
        3. **Provide Strategic Value**: Combine both sources for actionable insights
        
        4. **Structure for Clarity**: Use clear sections and professional formatting
        
        5. **Maintain Expert Voice**: Confident, knowledgeable, and helpful tone

        Create a response that showcases Zeron's expertise while providing comprehensive market intelligence.
        """
    
    @staticmethod
    def get_web_search_prompt():
        """Enhanced web search prompt with better targeting"""
        return """
        Conduct comprehensive web research for this query: "{query}"

        CONTEXT FROM ZERON (Internal Knowledge):
        {internal_context}

        RESEARCH OBJECTIVES:
        Based on the query and Zeron's context, search for:

        🔍 **Primary Research Areas:**
        1. **Direct Competitive Intelligence**
           - Specific competitors mentioned or implied
           - Feature comparisons and capability gaps
           - Competitive positioning and messaging
           - Recent product announcements or updates

        2. **Market & Industry Analysis**
           - Current market trends and growth patterns
           - Industry benchmarks and standards
           - Market sizing and forecast data
           - Key industry reports and analyst insights

        3. **Technical & Product Intelligence**
           - Technology trends and innovations
           - Integration capabilities and partnerships
           - Compliance and security standards
           - Best practices and methodologies

        4. **Business Intelligence**
           - Pricing models and packaging strategies
           - Customer case studies and use cases
           - Partnership announcements
           - Funding, acquisitions, or major business moves

        🎯 **Search Strategy:**
        - Prioritize recent information (last 12 months when possible)
        - Focus on authoritative sources (vendor sites, industry reports, analyst firms)
        - Look for specific, actionable intelligence rather than generic information
        - Include quantitative data where available (market size, growth rates, etc.)

        📊 **Output Requirements:**
        - Structure findings clearly with headers and sections
        - Include specific data points and metrics when available
        - Cite sources and recency of information
        - Highlight insights most relevant to Zeron's competitive position
        - Note any information gaps or areas requiring follow-up research

        Provide comprehensive, well-structured research that enables informed decision-making.
        """

    @staticmethod
    def get_rag_enhancement_prompt():
        """Prompt for enhancing RAG-only responses"""
        return """
        Enhance this internal knowledge response with strategic context and professional presentation.

        ORIGINAL QUERY: {query}

        INTERNAL KNOWLEDGE RESPONSE:
        {internal_answer}

        ENHANCEMENT OBJECTIVES:
        1. **Professional Structure**: Organize with clear headers and logical flow
        2. **Strategic Context**: Add market positioning and competitive context where relevant
        3. **Actionable Insights**: Include implementation guidance and best practices
        4. **Complete Coverage**: Ensure all aspects of the query are thoroughly addressed
        5. **Executive Perspective**: Present information at an appropriate strategic level

        Create a polished, comprehensive response that positions Zeron as a thought leader while fully addressing the user's query.
        """