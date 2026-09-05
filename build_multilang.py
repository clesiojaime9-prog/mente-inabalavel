import os
import base64
import json

def get_base64_image(image_path):
    with open(image_path, 'rb') as f:
        return 'data:image/webp;base64,' + base64.b64encode(f.read()).decode('utf-8')

b64_ebook = get_base64_image('/home/user/images/ebook-mockup.webp')
b64_bundle = get_base64_image('/home/user/images/bundle-mockup.webp')
b64_hero = get_base64_image('/home/user/images/hero-stoic.webp')

translations = {
    "BR": {
        "lang_code": "pt-BR",
        "country_name": "Brasil",
        "flag": "🇧🇷",
        "currency_symbol": "R$",
        "price_anchor": "R$ 97,00",
        "price_total": "R$ 147,00",
        "price_current": "R$ 19,90",
        "price_ebook": "R$ 67,00",
        "price_b1": "R$ 40,00",
        "price_b2": "R$ 40,00",
        "checkout_url": "https://pay.hotmart.com/B107479792A",
        "checkout_platform": "Hotmart",
        "payment_methods": "⚡ PIX Instantâneo • 💳 Cartão de Crédito • 📄 Boleto",
        "badge_top": "CONDIÇÃO EXCLUSIVA DE LANÇAMENTO NA HOTMART",
        "scarcity_text": "Restam apenas 7 vagas com preço promocional",
        "hook_badge": "GUIA OFICIAL DO PERFIL MENTE INABALÁVEL",
        "headline_start": "PARE DE",
        "headline_highlight": "NEGOCIAR COM VOCÊ MESMO",
        "headline_end": "E ASSUMA O CONTROLE.",
        "subheadline": "O sistema estoico e prático para homens que querem eliminar a procrastinação, dominar as próprias emoções e construir disciplina inabalável em 21 dias.",
        "image_badge": "📦 E-BOOK EM PDF + 2 BÔNUS PRÁTICOS • ACESSO IMEDIATO",
        "cta_hero": "QUERO ATIVAR MINHA MENTE INABALÁVEL",
        "trust_secure": "Compra 100% Segura via Hotmart",
        "trust_instant": "Acesso Imediato no E-mail",
        "trust_guarantee": "Garantia Incondicional de 7 Dias",
        "problem_badge": "A REALIDADE NUA E CRUA",
        "problem_title": "Você já sabe o que fazer.",
        "problem_title_red": "O problema é que você não faz.",
        "problem_p1": "Você não está aqui por falta de informação. Já sabe que precisa acordar no horário. Já sabe que o celular está te comendo vivo. Já sabe exatamente qual vício está te matando devagar.",
        "problem_p2": "À noite, assistindo a um vídeo com trilha épica no TikTok, você promete que <strong style='color:#fff'>'amanhã tudo vai ser diferente'</strong>. Sente aquele arrepio de motivação às 23h.",
        "problem_p3": "Mas às 6h da manhã, o arrepio já morreu. Você aperta o botão soneca. Rola o feed por 40 minutos. E se sente um lixo antes mesmo de escovar os dentes.",
        "problem_quote": "Motivação de rede social é um anestésico temporário. Sem um código de conduta interno, você vai continuar sendo escravo dos seus impulsos pelo resto da vida.",
        "turn_badge": "O PONTO DE VIRADA",
        "turn_title": "A culpa não é da sua força de vontade.",
        "turn_title_gold": "É da falta de um protocolo inegociável.",
        "turn_p1": "Você passa o dia travando uma guerra interna contra a sua própria mente. Cada tarefa simples vira uma negociação de 2 horas. Você tenta ser produtivo na base da 'força bruta' e termina o dia esgotado mentalmente.",
        "turn_p2": "Os homens que você admira não são seres humanos especiais dotados de superpoderes genéticos. Eles simplesmente possuem <strong style='color:#F59E0B'>regras que não são negociáveis</strong>.",
        "turn_p3": "Quando você remove a negociação da sua rotina, o cansaço mental desaparece e a execução se torna automática.",
        "pillar1_title": "Blindagem Emocional",
        "pillar1_desc": "Nunca mais reaja por impulso. Aprenda a controlar a dopamina barata, calar o ruído da opinião alheia e manter a postura imperturbável sob pressão extrema.",
        "pillar2_title": "Execução Fria",
        "pillar2_desc": "Faça o que precisa ser feito quando o alarme tocar, sem pestanejar, sem hesitar e sem precisar de 'vontade' para agir.",
        "quiz_badge": "TESTE RÁPIDO DE AUTODIAGNÓSTICO",
        "quiz_title": "Você tem o perfil de um Homem Inabalável?",
        "quiz_desc": "Selecione como você costuma agir nas 3 situações abaixo:",
        "q1_title": "1. O despertador toca às 05:30 da manhã no frio:",
        "q1_weak": "Aperto a soneca 3 vezes e fico 30min no feed",
        "q1_strong": "Levanto nos primeiros 5 segundos sem negociar",
        "q2_title": "2. Quando você recebe uma crítica ou ofensa na internet ou pessoalmente:",
        "q2_weak": "Fico irritado, respondo na hora e penso nisso o dia todo",
        "q2_strong": "Mantenho a postura estoica; o ruído alheio não me atinge",
        "q3_title": "3. Diante de um trabalho difícil que você precisa entregar:",
        "q3_weak": "Abro o Instagram/TikTok para 'descansar 5 min' e perco a tarde",
        "q3_strong": "Ativo o modo caverna até a missão estar 100% cumprida",
        "quiz_feedback_title": "⚠️ DIAGNÓSTICO: Você está operando com vazamento de disciplina.",
        "quiz_feedback_desc": "Se você marcou pelo menos 1 opção fraca, sua mente está no comando dos seus impulsos, e não você. O guia Mente Inabalável foi desenhado exatamente para reprogramar esses padrões.",
        "quiz_feedback_btn": "DESBLOQUEAR O CÓDIGO (R$ 19,90)",
        "features_badge": "CONTEÚDO PROGRAMÁTICO COMPLETO",
        "features_title": "O que você vai dominar dentro do livro:",
        "features_desc": "Um roteiro direto ao ponto, sem enrolação teórica ou clichês vazios de autoajuda.",
        "f1_title": "Capítulo 1: O Despertar da Consciência",
        "f1_desc": "Como identificar as mentiras sutis que você conta para si mesmo todos os dias e desmascarar a autoilusão.",
        "f2_title": "Capítulo 2: O Fim da Negociação Interna",
        "f2_desc": "A Regra dos 5 Segundos aplicada ao estoicismo para agir instantaneamente antes do cérebro sabotar.",
        "f3_title": "Capítulo 3: Blindagem contra o Ruído Externo",
        "f3_desc": "Técnicas milenares de Marco Aurélio para neutralizar fofocas, críticas destrutivas e a necessidade de validação social.",
        "f4_title": "Capítulo 4: O Poder do Silêncio e da Postura",
        "f4_desc": "Por que falar menos gera mais respeito magnético e autoridade natural em qualquer ambiente social.",
        "f5_title": "Capítulo 5: Foco Cirúrgico na Era da Distração",
        "f5_desc": "Como vencer a guerra da dopamina e recuperar 3 a 5 horas diárias que você perde nas redes sociais.",
        "f6_title": "Capítulo 6: O Código do Homem Implacável",
        "f6_desc": "O conjunto de 10 princípios inegociáveis para reger seu caráter, suas decisões financeiras e seus relacionamentos.",
        "auth_badge": "CONHEÇA O PROJETO",
        "auth_title": "Construído nos bastidores do",
        "auth_title_gold": "Perfil Mente Inabalável",
        "auth_desc": "Uma comunidade dedicada ao resgate da masculinidade sólida, foco de ferro e desenvolvimento pessoal prático.",
        "auth1": "Mais de 100 mil homens impactados diariamente por nossas pílulas de sabedoria estoica e disciplina.",
        "auth2": "Metodologia testada e validada em centenas de leitores reais que transformaram sua rotina e postura.",
        "auth3": "Sem enrolação, sem teorias complexas: direto ao ponto com protocolos aplicáveis no seu dia a dia.",
        "auth_footer": "Nosso lema: Menos desculpas, mais postura. Menos falação, mais resultados.",
        "offer_badge": "OFERTA COMPLETA DE LANÇAMENTO",
        "offer_title": "Tudo o que você vai receber hoje:",
        "offer_desc": "Adquirindo agora na Hotmart, você leva o livro principal + 2 bônus práticos exclusivos sem custo extra.",
        "offer_card_tag": "PACOTE COMPLETO DE TRANSFORMAÇÃO",
        "item1_title": "1. Livro Digital Oficial: Mente Inabalável (PDF)",
        "item1_desc": "O manual completo de 34 páginas com os 6 capítulos fundamentais, exercícios práticos e o código dos 10 princípios inegociáveis.",
        "item2_badge": "BÔNUS 1 • EXCLUSIVO",
        "item2_title": "2. Protocolo de 21 Dias de Desafio Prático",
        "item2_desc": "Um plano passo a passo com uma tarefa diária específica para implementar a blindagem mental na sua rotina e quebrar a inércia.",
        "item3_badge": "BÔNUS 2 • EXCLUSIVO",
        "item3_title": "3. Checklist Diário do Homem Focado",
        "item3_desc": "A ferramenta de acompanhamento rápido para imprimir ou salvar no celular e auditar sua consistência diária em 2 minutos.",
        "free_tag": "GRÁTIS HOJE",
        "included_tag": "INCLUSO",
        "total_val_label": "Valor Total de Mercado:",
        "promo_price_label": "Valor Promocional de Lançamento:",
        "payment_type_label": "Pagamento único • Acesso vitalício • Sem mensalidades",
        "cta_offer": "ATIVAR MEU CÓDIGO AGORA (R$ 19,90)",
        "secure_proc": "🔒 Processamento Oficial Seguro via Hotmart • Acesso Imediato",
        "compat_title": "📱 Formato 100% Digital e Acessível",
        "compat_desc": "Receba o material instantaneamente no seu e-mail após a aprovação da compra na Hotmart. Leia no smartphone (iOS/Android), tablet, Kindle ou computador. O arquivo é seu para sempre.",
        "not_for_title": "Para quem NÃO é este guia:",
        "not_for_1": "Pessoas que buscam fórmulas mágicas de sucesso sem fazer esforço diário.",
        "not_for_2": "Quem prefere continuar reclamando das circunstâncias e culpando o mundo.",
        "not_for_3": "Quem se ofende facilmente com verdades duras e autocrítica necessária.",
        "for_title": "Para quem É este guia:",
        "for_1": "Quem cansou de prometer mudanças para si mesmo e falhar no dia seguinte.",
        "for_2": "Quem deseja dominar suas emoções, parar de procrastinar e ter foco absoluto.",
        "for_3": "Homens que querem construir uma reputação de respeito, honra e solidez.",
        "guar_badge": "RISCO ZERO ABSOLUTO",
        "guar_title": "7 Dias de Garantia Incondicional Hotmart",
        "guar_desc": "Leia o material, aplique o Protocolo de 21 Dias e sinta a mudança na sua mente. Se por qualquer motivo você achar que o conteúdo não agregou valor brutal na sua vida, basta solicitar o reembolso na Hotmart com um clique. Devolvemos 100% do seu dinheiro.",
        "guar_bold": "Sem perguntas, sem burocracia e sem ressentimentos. O risco é todo meu.",
        "final_title": "A decisão que define o seu futuro",
        "final_title_gold": "é tomada AGORA.",
        "final_desc": "Enquanto você adia, a sua vida passa. Você pode continuar no mesmo ciclo de desculpas, ou investir <strong style='color:#F59E0B'>R$ 19,90</strong> agora na Hotmart e ativar o código que vai blindar a sua mente.",
        "final_cta": "SIM! QUERO SER UM HOMEM INABALÁVEL",
        "final_urgency": "⚡ Oferta por tempo limitado. O valor pode retornar para R$ 97,00 a qualquer momento.",
        "faq_badge": "TIRE SUAS DÚVIDAS",
        "faq_title": "Perguntas Frequentes",
        "faq1_q": "Como vou receber o material após a compra?",
        "faq1_a": "Assim que a compra for confirmada pela Hotmart (instantâneo no PIX e Cartão), você receberá um e-mail com o link direto para download do e-book em PDF de alta resolução e de todos os bônus inclusos.",
        "faq2_q": "Quais são as formas de pagamento disponíveis?",
        "faq2_a": "Você pode pagar com total segurança e garantia via PIX (aprovação imediata), Cartão de Crédito ou Boleto bancário diretamente na Hotmart por apenas R$ 19,90.",
        "faq3_q": "O e-book funciona no meu celular?",
        "faq3_a": "Sim! O livro digital foi diagramado e otimizado para leitura fluida tanto em celulares (iOS/Android) quanto em tablets, computadores e leitores digitais como Kindle.",
        "faq4_q": "E se eu não gostar do conteúdo?",
        "faq4_a": "Você está 100% protegido pela garantia incondicional de 7 dias da Hotmart. Basta pedir reembolso na plataforma e seu investimento será devolvido integralmente.",
        "faq5_q": "Eu terei que pagar mensalidade?",
        "faq5_a": "Não! O pagamento de R$ 19,90 é único e o acesso ao material é vitalício.",
        "sticky_btn": "COMPRAR NA HOTMART (R$ 19,90)"
    },
    "US": {
        "lang_code": "en-US",
        "country_name": "United States / Global",
        "flag": "🇺🇸",
        "currency_symbol": "$",
        "price_anchor": "$19.99",
        "price_total": "$29.99",
        "price_current": "$4.99",
        "price_ebook": "$15.00",
        "price_b1": "$7.50",
        "price_b2": "$7.50",
        "checkout_url": "https://pay.hotmart.com/B107479792A",
        "checkout_platform": "Hotmart",
        "payment_methods": "💳 Credit / Debit Cards • 🍏 Apple Pay • 🅿️ PayPal",
        "badge_top": "EXCLUSIVE LAUNCH OFFER ON HOTMART",
        "scarcity_text": "Only 7 spots remaining at launch price",
        "hook_badge": "OFFICIAL GUIDE FROM UNSHAKABLE MIND",
        "headline_start": "STOP",
        "headline_highlight": "NEGOTIATING WITH YOURSELF",
        "headline_end": "AND TAKE FULL CONTROL.",
        "subheadline": "The practical Stoic system for men who want to eliminate procrastination, master emotional control, and build relentless discipline in 21 days.",
        "image_badge": "📦 PDF E-BOOK + 2 PRACTICAL BONUSES • INSTANT ACCESS",
        "cta_hero": "I WANT TO UNLOCK MY UNSHAKABLE MIND",
        "trust_secure": "100% Secure Checkout via Hotmart",
        "trust_instant": "Instant Digital Access via Email",
        "trust_guarantee": "7-Day 100% Money-Back Guarantee",
        "problem_badge": "THE BRUTAL REALITY",
        "problem_title": "You already know what you need to do.",
        "problem_title_red": "The problem is you don't do it.",
        "problem_p1": "You are not here because of a lack of information. You already know you should wake up early. You already know your phone is draining your life. You know the bad habits holding you back.",
        "problem_p2": "At night, watching epic motivational clips on TikTok, you promise yourself that <strong style='color:#fff'>'tomorrow will be different'</strong>. You feel that rush of motivation at 11 PM.",
        "problem_p3": "By 6 AM, the motivation is completely gone. You hit snooze. You scroll social media for 40 minutes and feel like a failure before brushing your teeth.",
        "problem_quote": "Social media hype is just a temporary anesthetic. Without an internal code of conduct, you will remain a slave to your cheap impulses forever.",
        "turn_badge": "THE TURNING POINT",
        "turn_title": "It is not a lack of willpower.",
        "turn_title_gold": "It is the lack of a non-negotiable protocol.",
        "turn_p1": "You spend your days waging an exhausting mental war against yourself. Every single task becomes a 2-hour negotiation. You try to force progress and end the day completely drained.",
        "turn_p2": "The men you respect are not genetically gifted with superhuman strength. They simply live by <strong style='color:#F59E0B'>rules that are not open to negotiation</strong>.",
        "turn_p3": "When you eliminate internal debate, decision fatigue disappears and high performance becomes automatic.",
        "pillar1_title": "Emotional Armor",
        "pillar1_desc": "Never react on impulse again. Learn to curb cheap dopamine, silence the noise of other people's opinions, and remain calm under extreme pressure.",
        "pillar2_title": "Cold Execution",
        "pillar2_desc": "Do what must be done when the alarm rings, without blinking, without hesitating, and without waiting for 'motivation'.",
        "quiz_badge": "QUICK SELF-DIAGNOSTIC TEST",
        "quiz_title": "Do you have the mind of an Unshakable Man?",
        "quiz_desc": "Select how you usually react in these 3 real situations:",
        "q1_title": "1. The alarm goes off at 5:30 AM in the morning:",
        "q1_weak": "I hit snooze 3 times and scroll my phone for 30 min",
        "q1_strong": "I get up within 5 seconds without negotiating",
        "q2_title": "2. When someone criticizes or insults you online or in person:",
        "q2_weak": "I get angry, argue back, and dwell on it all day",
        "q2_strong": "I hold Stoic composure; external noise cannot penetrate me",
        "q3_title": "3. Facing a difficult task you must get done:",
        "q3_weak": "I open TikTok/Instagram for '5 minutes' and lose the afternoon",
        "q3_strong": "I enter cave mode until the mission is 100% complete",
        "quiz_feedback_title": "⚠️ DIAGNOSIS: You are operating with major discipline leaks.",
        "quiz_feedback_desc": "If you selected at least 1 weak option, your impulses are controlling you rather than you controlling them. The Unshakable Mind guide was designed to reprogram this pattern.",
        "quiz_feedback_btn": "UNLOCK THE CODE ($4.99)",
        "features_badge": "COMPLETE CURRICULUM",
        "features_title": "What you will master inside the book:",
        "features_desc": "A direct, practical blueprint with zero fluff or generic self-help cliches.",
        "f1_title": "Chapter 1: The Awakening of Awareness",
        "f1_desc": "Identify the subtle lies and rationalizations you tell yourself every single day.",
        "f2_title": "Chapter 2: The End of Self-Negotiation",
        "f2_desc": "The 5-Second Rule applied to Stoic mastery to act immediately before your brain sabotages you.",
        "f3_title": "Chapter 3: Shielding from External Noise",
        "f3_desc": "Ancient principles from Marcus Aurelius to neutralize drama, insults, and the craving for social validation.",
        "f4_title": "Chapter 4: The Power of Silence & Presence",
        "f4_desc": "Why speaking less builds magnetic authority, genuine respect, and calm dominance.",
        "f5_title": "Chapter 5: Surgical Focus in the Age of Distraction",
        "f5_desc": "Win the war on dopamine and reclaim 3 to 5 productive hours lost to social media addiction.",
        "f6_title": "Chapter 6: The Relentless Man's Code",
        "f6_desc": "The 10 non-negotiable principles to govern your daily habits, character, and life decisions.",
        "auth_badge": "BEHIND THE MOVEMENT",
        "auth_title": "Crafted by the team behind",
        "auth_title_gold": "Unshakable Mind",
        "auth_desc": "A global community dedicated to solid masculinity, unbreakable discipline, and practical growth.",
        "auth1": "Over 100,000 men reached daily with daily Stoic principles and actionable discipline frameworks.",
        "auth2": "Field-tested methods proven across hundreds of real readers who reshaped their daily focus.",
        "auth3": "No fluff, no complex theories: straight-to-the-point protocols you can apply immediately.",
        "auth_footer": "Our motto: Less talking, more posture. Fewer excuses, tangible results.",
        "offer_badge": "COMPLETE LAUNCH BUNDLE",
        "offer_title": "Everything you will receive today:",
        "offer_desc": "Order now via Hotmart and get the main guide + 2 exclusive actionable bonuses included at no extra cost.",
        "offer_card_tag": "COMPLETE TRANSFORMATION PACK",
        "item1_title": "1. Digital Book: Unshakable Mind (PDF)",
        "item1_desc": "The 34-page core manual covering 6 fundamental chapters, actionable exercises, and the 10-principle code.",
        "item2_badge": "BONUS 1 • EXCLUSIVE",
        "item2_title": "2. The 21-Day Practical Discipline Protocol",
        "item2_desc": "A day-by-day roadmap with one specific actionable challenge per day to build unstoppable momentum.",
        "item3_badge": "BONUS 2 • EXCLUSIVE",
        "item3_title": "3. Daily High-Focus Action Checklist",
        "item3_desc": "A 2-minute daily audit tool to track your consistency, habits, and focus straight from your phone or printout.",
        "free_tag": "FREE TODAY",
        "included_tag": "INCLUDED",
        "total_val_label": "Total Value:",
        "promo_price_label": "Special Launch Price:",
        "payment_type_label": "One-time payment • Lifetime access • No subscriptions",
        "cta_offer": "ACTIVATE MY ACCESS NOW ($4.99)",
        "secure_proc": "🔒 Official Secure Processing via Hotmart • Instant Access",
        "compat_title": "📱 100% Digital & Universal Format",
        "compat_desc": "Instant access delivered to your email right after checkout. Read on iPhone, Android, tablet, Kindle, or laptop. Yours forever.",
        "not_for_title": "Who this guide is NOT for:",
        "not_for_1": "Those seeking magic shortcuts without taking consistent daily action.",
        "not_for_2": "People who enjoy complaining and blaming circumstances for their problems.",
        "not_for_3": "Anyone easily offended by raw truths and honest self-critique.",
        "for_title": "Who this guide IS for:",
        "for_1": "Men tired of breaking promises to themselves and falling back into old habits.",
        "for_2": "Those seeking to master emotions, destroy procrastination, and build deep focus.",
        "for_3": "Those determined to build a solid reputation of respect, honor, and composure.",
        "guar_badge": "100% RISK-FREE",
        "guar_title": "7-Day 100% Money-Back Guarantee Hotmart",
        "guar_desc": "Read the book, test the 21-Day Protocol, and experience the mental shift. If you do not feel it delivered immense value, simply request a refund inside Hotmart with one click. You will get 100% of your money back.",
        "guar_bold": "No questions asked, no hassle. All risk is on us.",
        "final_title": "The decision that shapes your future",
        "final_title_gold": "is made RIGHT NOW.",
        "final_desc": "While you hesitate, life passes by. You can remain in the same cycle of excuses, or invest <strong style='color:#F59E0B'>$4.99</strong> on Hotmart right now to forge an unbreakable mindset.",
        "final_cta": "YES! I WANT TO BECOME UNSHAKABLE",
        "final_urgency": "⚡ Limited-time promotional price. Price may increase to $19.99 at any moment.",
        "faq_badge": "COMMON QUESTIONS",
        "faq_title": "Frequently Asked Questions",
        "faq1_q": "How will I receive the material after purchasing?",
        "faq1_a": "Instantly upon payment confirmation on Hotmart, you will receive an email with direct download access to the complete PDF guide and both bonus files.",
        "faq2_q": "What payment methods are supported?",
        "faq2_a": "You can pay securely with any major Credit/Debit Card, Apple Pay, Google Pay, or PayPal via Hotmart for just $4.99.",
        "faq3_q": "Does it work on smartphones?",
        "faq3_a": "Yes! The guide is formatted for seamless reading across all smartphones (iOS/Android), tablets, computers, and e-readers.",
        "faq4_q": "What if I am not satisfied?",
        "faq4_a": "You are fully protected by Hotmart's 7-Day Money-Back Guarantee. You can request a 100% refund with a single click.",
        "faq5_q": "Is there any monthly subscription fee?",
        "faq5_a": "No! This is a one-time payment of $4.99 with lifetime access and updates included.",
        "sticky_btn": "GET INSTANT ACCESS ($4.99)"
    },
    "ES": {
        "lang_code": "es-ES",
        "country_name": "España / Latam",
        "flag": "🇪🇸",
        "currency_symbol": "€",
        "price_anchor": "19,99€",
        "price_total": "29,99€",
        "price_current": "4,99€",
        "price_ebook": "15,00€",
        "price_b1": "7,50€",
        "price_b2": "7,50€",
        "checkout_url": "https://pay.hotmart.com/B107479792A",
        "checkout_platform": "Hotmart",
        "payment_methods": "💳 Tarjetas de Crédito / Débito • 🅿️ PayPal",
        "badge_top": "CONDICIÓN EXCLUSIVA DE LANZAMIENTO EN HOTMART",
        "scarcity_text": "Solo quedan 7 plazas con precio promocional",
        "hook_badge": "GUÍA OFICIAL DEL PERFIL MENTE INQUEBRANTABLE",
        "headline_start": "DEJA DE",
        "headline_highlight": "NEGOCIAR CONTIGO MISMO",
        "headline_end": "Y TOMA EL CONTROL.",
        "subheadline": "El sistema estoico y práctico para hombres que quieren eliminar la procrastinación, dominar sus emociones y construir disciplina inquebrantable en 21 días.",
        "image_badge": "📦 E-BOOK EN PDF + 2 BONOS PRÁCTICOS • ACCESO INMEDIATO",
        "cta_hero": "QUIERO ACTIVAR MI MENTE INQUEBRANTABLE",
        "trust_secure": "Compra 100% Segura a través de Hotmart",
        "trust_instant": "Acceso Inmediato a tu Correo",
        "trust_guarantee": "Garantía Incondicional de 7 Días",
        "problem_badge": "LA CRUDA REALIDAD",
        "problem_title": "Ya sabes exactamente lo que tienes que hacer.",
        "problem_title_red": "El problema es que no lo haces.",
        "problem_p1": "No estás aquí por falta de información. Ya sabes que debes levantarte temprano. Ya sabes que las redes sociales te están robando el tiempo. Conoces perfectamente los malos hábitos que te frenan.",
        "problem_p2": "Por la noche, viendo vídeos motivacionales en TikTok, te prometes que <strong style='color:#fff'>'mañana todo será diferente'</strong>. Sientes esa ráfaga de motivación a las 23:00.",
        "problem_p3": "Pero a las 6:00 de la mañana, la motivación ha desaparecido. Pulsas posponer alarma. Pasas 40 minutos en el móvil y te sientes frustrado antes de levantarte.",
        "problem_quote": "La motivación de internet es un anestésico pasajero. Sin un código de conducta interno, seguirás siendo esclavo de tus impulsos el resto de tu vida.",
        "turn_badge": "EL PUNTO DE INFLEXIÓN",
        "turn_title": "No es falta de fuerza de voluntad.",
        "turn_title_gold": "Es falta de un protocolo innegociable.",
        "turn_p1": "Pasas el día librando una agotadora batalla contra tu propia mente. Cada tarea se convierte en 2 horas de debate interno. Intentas avanzar por 'fuerza bruta' y terminas mentalmente agotado.",
        "turn_p2": "Los hombres que admiras no tienen superpoderes genéticos. Simplemente viven bajo <strong style='color:#F59E0B'>reglas que no se negocian</strong>.",
        "turn_p3": "Cuando eliminas la negociación de tu rutina, la fatiga mental desaparece y la ejecución se vuelve automática.",
        "pillar1_title": "Blindaje Emocional",
        "pillar1_desc": "Nunca más reacciones por impulso. Aprende a frenar la dopamina barata, silenciar las opiniones ajenas y mantener la calma bajo máxima presión.",
        "pillar2_title": "Ejecución Fría",
        "pillar2_desc": "Haz lo que tienes que hacer cuando suene la alarma, sin dudar, sin quejarte y sin depender de tener 'ganas'.",
        "quiz_badge": "TEST RÁPIDO DE AUTODIAGNÓSTICO",
        "quiz_title": "¿Tienes la mente de un Hombre Inquebrantable?",
        "quiz_desc": "Selecciona cómo sueles actuar ante estas 3 situaciones cotidianas:",
        "q1_title": "1. Suena el despertador a las 5:30 de la mañana:",
        "q1_weak": "Pospongo 3 veces y paso 30 min en el feed del móvil",
        "q1_strong": "Me levanto en los primeros 5 segundos sin negociar",
        "q2_title": "2. Cuando recibes una crítica o insulto en internet o en persona:",
        "q2_weak": "Me enfado, respondo al instante y me obsesiono todo el día",
        "q2_strong": "Mantengo la postura estoica; el ruido ajeno no me afecta",
        "q3_title": "3. Ante una tarea compleja que debes entregar:",
        "q3_weak": "Abro Instagram/TikTok '5 minutos' y pierdo toda la tarde",
        "q3_strong": "Activo el modo caverna hasta que la misión esté 100% cumplida",
        "quiz_feedback_title": "⚠️ DIAGNÓSTICO: Estás operando con fugas críticas de disciplina.",
        "quiz_feedback_desc": "Si marcaste al menos 1 opción débil, tus impulsos te dominan a ti en vez de tú a ellos. La guía Mente Inquebrantable fue diseñada para reprogramar este patrón.",
        "quiz_feedback_btn": "DESBLOQUEAR EL CÓDIGO (4,99€)",
        "features_badge": "CONTENIDO COMPLETO",
        "features_title": "Lo que vas a dominar dentro del libro:",
        "features_desc": "Una guía directa, práctica y sin rodeos teóricos ni clichés de autoayuda.",
        "f1_title": "Capítulo 1: El Despertar de la Consciencia",
        "f1_desc": "Identifica las trampas y excusas sutiles que te cuentas a ti mismo a diario.",
        "f2_title": "Capítulo 2: El Fin de la Negociación Interna",
        "f2_desc": "La Regla de los 5 Segundos aplicada al estoicismo para actuar antes de que tu mente te sabotee.",
        "f3_title": "Capítulo 3: Blindaje contra el Ruido Externo",
        "f3_desc": "Principios de Marco Aurelio para neutralizar críticas, chismes y la necesidad de aprobación social.",
        "f4_title": "Capítulo 4: El Poder del Silencio y la Presencia",
        "f4_desc": "Por qué hablar menos genera mayor respeto magnético y autoridad natural.",
        "f5_title": "Capítulo 5: Enfoque Quirúrgico en la Era de la Distracción",
        "f5_desc": "Vence la adicción a la dopamina barata y recupera de 3 a 5 horas diarias perdidas en el móvil.",
        "f6_title": "Capítulo 6: El Código del Hombre Implacable",
        "f6_desc": "Los 10 principios innegociables para gobernar tu carácter, hábitos y decisiones de vida.",
        "auth_badge": "CONOCE EL PROYECTO",
        "auth_title": "Creado por el equipo de",
        "auth_title_gold": "Mente Inquebrantable",
        "auth_desc": "Una comunidad dedicada a rescatar la solidez masculina, el carácter firme y el crecimiento personal práctico.",
        "auth1": "Más de 100.000 hombres impactados a diario con píldoras de sabiduría estoica y disciplina.",
        "auth2": "Metodologia comprobada por cientos de lectores reales que transformaron su enfoque y postura.",
        "auth3": "Sin rodeos ni teorías complejas: protocolos directos aplicables a tu vida real hoy mismo.",
        "auth_footer": "Nuestro lema: Menos excusas, más presencia. Menos palabras, más resultados.",
        "offer_badge": "OFERTA COMPLETA DE LANZAMIENTO",
        "offer_title": "Todo lo que recibirás hoy:",
        "offer_desc": "Al ordenar hoy en Hotmart, recibes el libro principal + 2 bonos prácticos exclusivos sin coste adicional.",
        "offer_card_tag": "PAQUETE COMPLETO DE TRANSFORMACIÓN",
        "item1_title": "1. Libro Digital: Mente Inquebrantable (PDF)",
        "item1_desc": "El manual central de 34 páginas con los 6 capítulos fundamentales, ejercicios prácticos y el código de 10 principios.",
        "item2_badge": "BONO 1 • EXCLUSIVO",
        "item2_title": "2. Protocolo de 21 Días de Desafío Práctico",
        "item2_desc": "Un plan diario paso a paso con una misión específica por día para blindar tu mente y romper la inercia.",
        "item3_badge": "BONO 2 • EXCLUSIVO",
        "item3_title": "3. Checklist Diario del Hombre Enfocado",
        "item3_desc": "Herramienta de auditoría rápida para imprimir o guardar en tu móvil y revisar tu disciplina en 2 minutos.",
        "free_tag": "GRATIS HOY",
        "included_tag": "INCLUIDO",
        "total_val_label": "Valor Total:",
        "promo_price_label": "Precio Especial de Lanzamiento:",
        "payment_type_label": "Pago único • Acceso de por vida • Sin suscripciones",
        "cta_offer": "ACTIVAR MI CÓDIGO AHORA (4,99€)",
        "secure_proc": "🔒 Procesamiento Oficial Seguro vía Hotmart • Acceso Inmediato",
        "compat_title": "📱 Formato 100% Digital y Universal",
        "compat_desc": "Recibe el material al instante en tu correo electrónico tras la compra en Hotmart. Léelo en tu móvil (iOS/Android), tablet, Kindle u ordenador. Tuyo para siempre.",
        "not_for_title": "Para quién NO es este libro:",
        "not_for_1": "Quienes buscan atajos mágicos sin esforzarse ni actuar con disciplina.",
        "not_for_2": "Personas que prefieren quejarse y culpar al entorno de su situación.",
        "not_for_3": "Cualquiera que se ofenda fácilmente con verdades directas y autocrítica sincera.",
        "for_title": "Para quién SÍ es este libro:",
        "for_1": "Quienes están hartos de prometerse cambios y recaer en los mismos errores al día siguiente.",
        "for_2": "Quienes quieren dominar sus emociones, frenar la procrastinación y tener enfoque absoluto.",
        "for_3": "Hombres decididos a construir una reputación de respeto, honor y solidez.",
        "guar_badge": "RIESGO CERO ABSOLUTO",
        "guar_title": "Garantía Incondicional de 7 Días Hotmart",
        "guar_desc": "Lee el libro, aplica el Protocolo de 21 Días y comprueba el cambio mental. Si por cualquier motivo sientes que no te aportó un valor enorme, solicita el reembolso en Hotmart con un solo clic. Te devolvemos el 100% de tu dinero.",
        "guar_bold": "Sin preguntas ni complicaciones. Todo el riesgo corre por nuestra cuenta.",
        "final_title": "La decisión que definirá tu futuro",
        "final_title_gold": "se toma AHORA.",
        "final_desc": "Mientras dudas, la vida pasa. Puedes seguir en el mismo círculo de excusas, o invertir <strong style='color:#F59E0B'>4,99€</strong> en Hotmart ahora y forjar una mentalidad inquebrantable.",
        "final_cta": "¡SÍ! QUIERO SER UN HOMBRE INQUEBRANTABLE",
        "final_urgency": "⚡ Oferta por tiempo limitado. El precio puede subir a 19,99€ en cualquier momento.",
        "faq_badge": "PREGUNTAS FRECUENTES",
        "faq_title": "Preguntas Frecuentes",
        "faq1_q": "¿Cómo recibiré el material tras la compra?",
        "faq1_a": "Inmediatamente después de confirmar tu pago en Hotmart, recibirás un correo electrónico con el enlace directo para descargar el e-book en PDF y ambos bonos.",
        "faq2_q": "¿Qué métodos de pago están disponibles?",
        "faq2_a": "Puedes pagar de forma 100% segura mediante tarjeta de crédito/débito o PayPal directamente en Hotmart por solo 4,99€.",
        "faq3_q": "¿Funciona en mi móvil?",
        "faq3_a": "¡Sí! El libro digital está optimizado para leerse cómodamente en cualquier smartphone (iOS/Android), tablet, ordenador o Kindle.",
        "faq4_q": "¿Qué pasa si no me gusta?",
        "faq4_a": "Estás respaldado por la garantía incondicional de 7 días de Hotmart. Pides el reembolso en la plataforma y recuperas el 100% de tu dinero.",
        "faq5_q": "¿Hay algún pago recurrente o mensualidad?",
        "faq5_a": "¡No! Es un pago único de 4,99€ con acceso para siempre.",
        "sticky_btn": "COMPRAR EN HOTMART (4,99€)"
    }
}

html_template = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mente Inabalável — O Código do Homem Frio, Focado e Implacável | Hotmart</title>
  
  <meta name="description" content="O sistema estoico e prático para homens que querem eliminar a procrastinação, dominar as emoções e construir disciplina inabalável em 21 dias.">
  <meta name="keywords" content="mente inabalável, estoicismo, disciplina, foco, alta performance, desenvolvimento pessoal, hotmart">
  <meta property="og:title" content="Mente Inabalável — O Código do Homem Frio, Focado e Implacável">
  <meta property="og:description" content="Elimine a procrastinação e construa disciplina inabalável em 21 dias. Acesse agora pela Hotmart.">
  <meta property="og:type" content="website">

  <!-- Inter Font -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">

  <style>
    /* ========================================================================= */
    /* RESET & CORE VARIABLES */
    /* ========================================================================= */
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    :root {{
      --bg-dark: #07080B;
      --bg-card: #0F121C;
      --bg-card-hover: #151A29;
      --gold-primary: #F59E0B;
      --gold-hover: #D97706;
      --gold-glow: rgba(245, 158, 11, 0.28);
      --text-white: #FFFFFF;
      --text-gray: #94A3B8;
      --text-muted: #64748B;
      --border-dark: rgba(255, 255, 255, 0.08);
      --border-gold: rgba(245, 158, 11, 0.35);
      --red-accent: #EF4444;
      --green-accent: #10B981;
    }}

    body {{
      background-color: var(--bg-dark);
      color: var(--text-white);
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      line-height: 1.6;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }}

    /* Global Watermark Blocker */
    body::after, body::before, div[class*="lovable"], div[id*="lovable"],
    a[href*="lovable.dev"], iframe[src*="lovable"] {{
      display: none !important;
      visibility: hidden !important;
      opacity: 0 !important;
      pointer-events: none !important;
    }}

    /* Utilities */
    .container-custom {{
      width: 100%;
      max-width: 680px;
      margin: 0 auto;
      padding: 0 1.25rem;
    }}

    .gold-gradient-text {{
      background: linear-gradient(135deg, #FFFBEB 0%, #F59E0B 50%, #D97706 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .red-gradient-text {{
      background: linear-gradient(135deg, #FEE2E2 0%, #EF4444 60%, #B91C1C 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    /* Buttons */
    .btn-gold {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.6rem;
      width: 100%;
      background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
      color: #000000;
      font-weight: 900;
      font-size: 1.05rem;
      letter-spacing: 0.03em;
      text-transform: uppercase;
      padding: 1.15rem 1.75rem;
      border-radius: 0.85rem;
      text-decoration: none;
      border: 1px solid #FDE68A;
      box-shadow: 0 10px 25px -5px rgba(245, 158, 11, 0.4), 0 0 15px rgba(245, 158, 11, 0.2);
      transition: all 0.25s ease;
      cursor: pointer;
    }}

    .btn-gold:hover {{
      transform: translateY(-2px);
      box-shadow: 0 15px 35px -5px rgba(245, 158, 11, 0.6), 0 0 25px rgba(245, 158, 11, 0.4);
      background: linear-gradient(135deg, #FBBF24 0%, #EA580C 100%);
    }}

    .pulse-glow {{
      animation: pulseGlow 2.5s infinite;
    }}

    @keyframes pulseGlow {{
      0% {{ box-shadow: 0 0 0 0 rgba(245, 158, 11, 0.6); }}
      70% {{ box-shadow: 0 0 0 14px rgba(245, 158, 11, 0); }}
      100% {{ box-shadow: 0 0 0 0 rgba(245, 158, 11, 0); }}
    }}

    /* Card Box */
    .glass-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-dark);
      border-radius: 1.25rem;
      padding: 1.5rem;
      transition: border-color 0.25s ease, transform 0.25s ease;
    }}

    .glass-card:hover {{
      border-color: rgba(245, 158, 11, 0.3);
    }}

    /* Badge Pills */
    .badge-pill {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.72rem;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 0.35rem 0.85rem;
      border-radius: 2rem;
    }}

    .badge-gold {{
      background: rgba(245, 158, 11, 0.12);
      border: 1px solid rgba(245, 158, 11, 0.35);
      color: #F59E0B;
    }}

    .badge-red {{
      background: rgba(239, 68, 68, 0.12);
      border: 1px solid rgba(239, 68, 68, 0.35);
      color: #EF4444;
    }}

    .badge-green {{
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid rgba(16, 185, 129, 0.35);
      color: #10B981;
    }}

    /* Country Switcher & Modal */
    .country-selector-pill {{
      display: inline-flex;
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.12);
      border-radius: 2rem;
      padding: 0.2rem;
      gap: 0.2rem;
    }}

    .country-btn {{
      background: transparent;
      border: none;
      color: #94A3B8;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.35rem 0.75rem;
      border-radius: 1.5rem;
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
    }}

    .country-btn.active {{
      background: var(--gold-primary);
      color: #000000;
      box-shadow: 0 2px 8px rgba(245, 158, 11, 0.4);
    }}

    /* Fullscreen Modal */
    #countryModal {{
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.88);
      backdrop-filter: blur(8px);
      z-index: 9999;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1rem;
      animation: fadeIn 0.3s ease;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: scale(0.96); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}

    .modal-country-card {{
      background: #0D111A;
      border: 1px solid rgba(245, 158, 11, 0.4);
      border-radius: 1.25rem;
      padding: 2rem 1.5rem;
      max-width: 440px;
      width: 100%;
      text-align: center;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.9), 0 0 30px rgba(245, 158, 11, 0.2);
    }}

    .modal-country-option {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: #151A26;
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 1rem 1.25rem;
      border-radius: 0.85rem;
      margin-bottom: 0.75rem;
      cursor: pointer;
      transition: all 0.2s ease;
      text-align: left;
    }}

    .modal-country-option:hover {{
      border-color: #F59E0B;
      background: #1A2234;
      transform: translateX(4px);
    }}

    /* Quiz Radio Interactive */
    .quiz-option {{
      display: flex;
      align-items: center;
      gap: 0.85rem;
      background: #121622;
      border: 1px solid var(--border-dark);
      padding: 0.9rem 1.15rem;
      border-radius: 0.75rem;
      margin-bottom: 0.6rem;
      cursor: pointer;
      transition: all 0.2s ease;
      text-align: left;
      font-size: 0.92rem;
    }}

    .quiz-option:hover {{
      border-color: rgba(245, 158, 11, 0.4);
      background: #171E2E;
    }}

    .quiz-option.selected-weak {{
      border-color: #EF4444;
      background: rgba(239, 68, 68, 0.1);
    }}

    .quiz-option.selected-strong {{
      border-color: #F59E0B;
      background: rgba(245, 158, 11, 0.12);
    }}

    .radio-circle {{
      width: 20px;
      height: 20px;
      border-radius: 50%;
      border: 2px solid #475569;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      font-size: 0.7rem;
      font-weight: 900;
    }}

    /* FAQ Accordion */
    details {{
      background: var(--bg-card);
      border: 1px solid var(--border-dark);
      border-radius: 0.85rem;
      margin-bottom: 0.75rem;
      overflow: hidden;
      transition: border-color 0.2s ease;
    }}

    details[open] {{
      border-color: rgba(245, 158, 11, 0.4);
      background: #121724;
    }}

    summary {{
      padding: 1.15rem 1.25rem;
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      list-style: none;
      user-select: none;
    }}

    summary::-webkit-details-marker {{
      display: none;
    }}

    summary::after {{
      content: '+';
      font-size: 1.3rem;
      font-weight: 400;
      color: #F59E0B;
      transition: transform 0.2s ease;
    }}

    details[open] summary::after {{
      content: '−';
      transform: rotate(180deg);
    }}

    .faq-answer {{
      padding: 0 1.25rem 1.15rem 1.25rem;
      color: var(--text-gray);
      font-size: 0.88rem;
      line-height: 1.6;
      border-top: 1px solid rgba(255, 255, 255, 0.04);
      padding-top: 0.85rem;
    }}

    /* Sticky Bottom Bar */
    .sticky-buy-bar {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(11, 14, 23, 0.95);
      backdrop-filter: blur(12px);
      border-top: 1px solid rgba(245, 158, 11, 0.35);
      padding: 0.75rem 1rem;
      z-index: 90;
      display: flex;
      align-items: center;
      justify-content: space-between;
      box-shadow: 0 -10px 25px rgba(0,0,0,0.7);
    }}
  </style>
</head>

<body>

  <!-- ========================================================================= -->
  <!-- COUNTRY MODAL ON FIRST VISIT (BR / US / ES) -->
  <!-- ========================================================================= -->
  <div id="countryModal" style="display: none;">
    <div class="modal-country-card">
      <div style="width: 50px; height: 50px; margin: 0 auto 1rem auto; background: rgba(245,158,11,0.2); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; border: 1px solid rgba(245,158,11,0.5);">
        🌎
      </div>
      
      <h2 style="font-size: 1.25rem; font-weight: 900; color: #FFFFFF; text-transform: uppercase; margin-bottom: 0.35rem;">
        SELECIONE SEU PAÍS
      </h2>
      <p style="font-size: 0.78rem; color: #94A3B8; margin-bottom: 1.5rem;">
        Select your country / Selecciona tu país para ver en tu moneda:
      </p>

      <div style="display: flex; flex-direction: column;">
        <!-- Option BR -->
        <div onclick="selectCountry('BR')" class="modal-country-option">
          <div style="display: flex; align-items: center; gap: 0.75rem;">
            <span style="font-size: 1.6rem;">🇧🇷</span>
            <div>
              <strong style="color: #FFFFFF; font-size: 0.95rem; display: block;">Brasil (BR)</strong>
              <span style="font-size: 0.72rem; color: #94A3B8;">PIX, Cartão e Boleto • R$ 19,90</span>
            </div>
          </div>
          <span style="color: #F59E0B; font-weight: 800; font-size: 0.95rem;">→</span>
        </div>

        <!-- Option US -->
        <div onclick="selectCountry('US')" class="modal-country-option">
          <div style="display: flex; align-items: center; gap: 0.75rem;">
            <span style="font-size: 1.6rem;">🇺🇸</span>
            <div>
              <strong style="color: #FFFFFF; font-size: 0.95rem; display: block;">United States / Global (US)</strong>
              <span style="font-size: 0.72rem; color: #94A3B8;">English • Card / PayPal / Apple Pay • $4.99</span>
            </div>
          </div>
          <span style="color: #F59E0B; font-weight: 800; font-size: 0.95rem;">→</span>
        </div>

        <!-- Option ES -->
        <div onclick="selectCountry('ES')" class="modal-country-option">
          <div style="display: flex; align-items: center; gap: 0.75rem;">
            <span style="font-size: 1.6rem;">🇪🇸</span>
            <div>
              <strong style="color: #FFFFFF; font-size: 0.95rem; display: block;">España / Latam (ES)</strong>
              <span style="font-size: 0.72rem; color: #94A3B8;">Español • Tarjeta / PayPal • 4,99€</span>
            </div>
          </div>
          <span style="color: #F59E0B; font-weight: 800; font-size: 0.95rem;">→</span>
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- 0. TOP URGENCY / SCARCITY BANNER + COUNTRY PICKER IN HEADER -->
  <!-- ========================================================================= -->
  <header style="background: #0B0E17; border-bottom: 1px solid rgba(245, 158, 11, 0.25); padding: 0.65rem 1rem; position: sticky; top: 0; z-index: 100; backdrop-filter: blur(10px);">
    <div style="max-width: 680px; margin: 0 auto; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.5rem; text-align: center;">
      
      <!-- Country Switcher Pill -->
      <div class="country-selector-pill" style="margin: 0 auto;">
        <button id="btn-BR" onclick="selectCountry('BR')" class="country-btn active">🇧🇷 BR (R$)</button>
        <button id="btn-US" onclick="selectCountry('US')" class="country-btn">🇺🇸 US ($)</button>
        <button id="btn-ES" onclick="selectCountry('ES')" class="country-btn">🇪🇸 ES (€)</button>
      </div>

      <div style="display: flex; align-items: center; gap: 0.75rem; font-size: 0.75rem; margin: 0 auto;">
        <span style="color: #94A3B8;">Timer:</span>
        <span id="countdown" style="font-family: monospace; font-weight: 900; background: #000; color: #F59E0B; padding: 0.15rem 0.5rem; border-radius: 0.35rem; border: 1px solid rgba(245, 158, 11, 0.4);">
          14:59
        </span>
        <span id="t-scarcity" style="color: #10B981; font-weight: 700;">• Restam apenas 7 vagas com preço promocional</span>
      </div>
    </div>
  </header>

  <!-- ========================================================================= -->
  <!-- HERO SECTION -->
  <!-- ========================================================================= -->
  <section style="position: relative; padding-top: 2rem; padding-bottom: 3.5rem; overflow: hidden;">
    <div style="position: absolute; top: -100px; left: 50%; transform: translateX(-50%); width: 500px; height: 500px; background: radial-gradient(circle, rgba(245,158,11,0.15) 0%, rgba(7,8,11,0) 70%); pointer-events: none;"></div>

    <div class="container-custom" style="text-align: center; position: relative; z-index: 2;">
      
      <!-- TikTok Hook Badge -->
      <div class="badge-pill badge-gold" style="margin-bottom: 1.25rem;">
        <svg width="14" height="14" viewBox="0 0 20 20" fill="currentColor" style="color: #F59E0B;">
          <path fill-rule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.381z" clip-rule="evenodd"/>
        </svg>
        <span id="t-hook-badge">GUIA OFICIAL DO PERFIL MENTE INABALÁVEL</span>
      </div>

      <!-- Main VSL Headline -->
      <h1 style="font-size: clamp(1.85rem, 5.5vw, 2.75rem); font-weight: 900; line-height: 1.15; letter-spacing: -0.03em; margin-bottom: 1.25rem; text-transform: uppercase;">
        <span id="t-headline-start">PARE DE</span> <span id="t-headline-highlight" class="red-gradient-text">NEGOCIAR COM VOCÊ MESMO</span> <span id="t-headline-end">E ASSUMA O CONTROLE.</span>
      </h1>

      <!-- Subheadline -->
      <p id="t-subheadline" style="font-size: clamp(0.95rem, 2.5vw, 1.1rem); color: var(--text-gray); line-height: 1.6; max-width: 580px; margin: 0 auto 2rem auto;">
        O sistema estoico e prático para homens que querem eliminar a procrastinação, dominar as próprias emoções e construir disciplina inabalável em 21 dias.
      </p>

      <!-- 3D Book Presentation Container -->
      <div style="position: relative; margin-bottom: 2rem; display: inline-block; width: 100%; max-width: 440px;">
        <div style="position: absolute; inset: 0; background: radial-gradient(circle, rgba(245,158,11,0.25) 0%, rgba(0,0,0,0) 70%); filter: blur(25px); z-index: 1;"></div>
        <img src="{b64_ebook}" alt="E-book Mente Inabalável Mockup 3D" style="width: 100%; max-width: 360px; height: auto; position: relative; z-index: 2; filter: drop-shadow(0 20px 30px rgba(0,0,0,0.8)); border-radius: 12px; transition: transform 0.3s ease;">
        <div style="position: absolute; bottom: -10px; left: 50%; transform: translateX(-50%); z-index: 3; background: #0B0E17; border: 1px solid rgba(245, 158, 11, 0.5); padding: 0.35rem 1rem; border-radius: 2rem; font-size: 0.72rem; font-weight: 800; color: #F59E0B; white-space: nowrap; box-shadow: 0 4px 15px rgba(0,0,0,0.5);">
          <span id="t-image-badge">📦 E-BOOK EM PDF + 2 BÔNUS PRÁTICOS • ACESSO IMEDIATO</span>
        </div>
      </div>

      <!-- Main Anchor Pricing Box in Hero -->
      <div style="background: rgba(15, 18, 28, 0.85); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 1rem; padding: 1.25rem; margin-bottom: 1.5rem; max-width: 480px; margin-left: auto; margin-right: auto;">
        <div style="display: flex; align-items: center; justify-content: center; gap: 0.75rem; margin-bottom: 0.5rem;">
          <span id="t-price-anchor" style="color: #64748B; text-decoration: line-through; font-size: 1.1rem; font-weight: 600;">De R$ 97,00</span>
          <span id="t-price-current" style="color: #F59E0B; font-size: 1.85rem; font-weight: 900;">Por apenas R$ 19,90</span>
        </div>
        <a id="t-cta-hero-btn" href="https://pay.hotmart.com/B107479792A" target="_blank" class="btn-gold pulse-glow" style="max-width: 480px; margin: 0 auto;">
          <span id="t-cta-hero">QUERO ATIVAR MINHA MENTE INABALÁVEL</span>
          <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/>
          </svg>
        </a>
      </div>

      <!-- Trust Badges -->
      <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem 1.5rem; font-size: 0.78rem; color: #94A3B8; margin-top: 1rem;">
        <span style="display: flex; align-items: center; gap: 0.35rem;">
          <svg width="15" height="15" viewBox="0 0 20 20" fill="#10B981"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l5-5z" clip-rule="evenodd"/></svg>
          <span id="t-trust-secure">Compra 100% Segura via Hotmart</span>
        </span>
        <span style="display: flex; align-items: center; gap: 0.35rem;">
          <svg width="15" height="15" viewBox="0 0 20 20" fill="#10B981"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l5-5z" clip-rule="evenodd"/></svg>
          <span id="t-trust-instant">Acesso Imediato no E-mail</span>
        </span>
        <span style="display: flex; align-items: center; gap: 0.35rem;">
          <svg width="15" height="15" viewBox="0 0 20 20" fill="#10B981"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l5-5z" clip-rule="evenodd"/></svg>
          <span id="t-trust-guarantee">Garantia Incondicional de 7 Dias</span>
        </span>
      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 1. PROBLEM / AGITATION SECTION -->
  <!-- ========================================================================= -->
  <section style="padding: 3rem 0; background: #0A0D15; border-top: 1px solid var(--border-dark); border-bottom: 1px solid var(--border-dark);">
    <div class="container-custom">
      
      <div style="text-align: center; margin-bottom: 2rem;">
        <div class="badge-pill badge-red" style="margin-bottom: 0.75rem;">
          <span id="t-problem-badge">A REALIDADE NUA E CRUA</span>
        </div>
        <h2 style="font-size: clamp(1.5rem, 4vw, 2rem); font-weight: 800; line-height: 1.25;">
          <span id="t-problem-title">Você já sabe o que fazer.</span><br>
          <span id="t-problem-title-red" class="red-gradient-text">O problema é que você não faz.</span>
        </h2>
      </div>

      <div class="glass-card" style="border-left: 4px solid #EF4444; margin-bottom: 1.5rem;">
        <p id="t-problem-p1" style="color: #CBD5E1; font-size: 0.95rem; margin-bottom: 1rem; line-height: 1.7;">
          Você não está aqui por falta de informação. Já sabe que precisa acordar no horário. Já sabe que o celular está te comendo vivo. Já sabe exatamente qual vício está te matando devagar.
        </p>
        <p id="t-problem-p2" style="color: #CBD5E1; font-size: 0.95rem; margin-bottom: 1rem; line-height: 1.7;">
          À noite, assistindo a um vídeo com trilha épica no TikTok, você promete que <strong style='color:#fff'>'amanhã tudo vai ser diferente'</strong>. Sente aquele arrepio de motivação às 23h.
        </p>
        <p id="t-problem-p3" style="color: #CBD5E1; font-size: 0.95rem; line-height: 1.7;">
          Mas às 6h da manhã, o arrepio já morreu. Você aperta o botão soneca. Rola o feed por 40 minutos. E se sente um lixo antes mesmo de escovar os dentes.
        </p>
      </div>

      <div style="background: rgba(239, 68, 68, 0.08); border: 1px dashed rgba(239, 68, 68, 0.35); border-radius: 0.85rem; padding: 1.25rem; text-align: center;">
        <p id="t-problem-quote" style="font-size: 0.88rem; color: #FCA5A5; font-style: italic; font-weight: 500;">
          "Motivação de rede social é um anestésico temporário. Sem um código de conduta interno, você vai continuar sendo escravo dos seus impulsos pelo resto da vida."
        </p>
      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 2. THE TURNING POINT (THE STOIC SOLUTION) -->
  <!-- ========================================================================= -->
  <section style="padding: 3.5rem 0; position: relative;">
    <div class="container-custom">
      
      <div style="text-align: center; margin-bottom: 2.25rem;">
        <div class="badge-pill badge-gold" style="margin-bottom: 0.75rem;">
          <span id="t-turn-badge">O PONTO DE VIRADA</span>
        </div>
        <h2 style="font-size: clamp(1.45rem, 4vw, 1.95rem); font-weight: 800; line-height: 1.25;">
          <span id="t-turn-title">A culpa não é da sua força de vontade.</span><br>
          <span id="t-turn-title-gold" class="gold-gradient-text">É da falta de um protocolo inegociável.</span>
        </h2>
      </div>

      <div style="display: flex; flex-direction: column; gap: 1.25rem; margin-bottom: 2rem;">
        <div class="glass-card">
          <p id="t-turn-p1" style="color: #CBD5E1; font-size: 0.92rem; line-height: 1.7; margin-bottom: 0.75rem;">
            Você passa o dia travando uma guerra interna contra a sua própria mente. Cada tarefa simples vira uma negociação de 2 horas. Você tenta ser produtivo na base da 'força bruta' e termina o dia esgotado mentalmente.
          </p>
          <p id="t-turn-p2" style="color: #CBD5E1; font-size: 0.92rem; line-height: 1.7; margin-bottom: 0.75rem;">
            Os homens que você admira não são seres humanos especiais dotados de superpoderes genéticos. Eles simplesmente possuem <strong style='color:#F59E0B'>regras que não são negociáveis</strong>.
          </p>
          <p id="t-turn-p3" style="color: #CBD5E1; font-size: 0.92rem; line-height: 1.7;">
            Quando você remove a negociação da sua rotina, o cansaço mental desaparece e a execução se torna automática.
          </p>
        </div>
      </div>

      <!-- Two Pillars -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem;">
        
        <div class="glass-card" style="border-top: 3px solid #F59E0B;">
          <div style="font-size: 1.85rem; margin-bottom: 0.5rem;">🛡️</div>
          <h3 id="t-pillar1-title" style="font-size: 1.1rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.5rem;">
            Blindagem Emocional
          </h3>
          <p id="t-pillar1-desc" style="color: var(--text-gray); font-size: 0.85rem; line-height: 1.6;">
            Nunca mais reaja por impulso. Aprenda a controlar a dopamina barata, calar o ruído da opinião alheia e manter a postura imperturbável sob pressão extrema.
          </p>
        </div>

        <div class="glass-card" style="border-top: 3px solid #F59E0B;">
          <div style="font-size: 1.85rem; margin-bottom: 0.5rem;">⚡</div>
          <h3 id="t-pillar2-title" style="font-size: 1.1rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.5rem;">
            Execução Fria
          </h3>
          <p id="t-pillar2-desc" style="color: var(--text-gray); font-size: 0.85rem; line-height: 1.6;">
            Faça o que precisa ser feito quando o alarme tocar, sem pestanejar, sem hesitar e sem precisar de 'vontade' para agir.
          </p>
        </div>

      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 3. INTERACTIVE QUIZ DIAGNOSTIC (TIKTOK STYLE) -->
  <!-- ========================================================================= -->
  <section style="padding: 3rem 0; background: #0B0E18; border-top: 1px solid var(--border-dark); border-bottom: 1px solid var(--border-dark);">
    <div class="container-custom">
      
      <div style="text-align: center; margin-bottom: 1.75rem;">
        <div class="badge-pill badge-gold" style="margin-bottom: 0.6rem;">
          <span id="t-quiz-badge">TESTE RÁPIDO DE AUTODIAGNÓSTICO</span>
        </div>
        <h2 id="t-quiz-title" style="font-size: clamp(1.35rem, 3.8vw, 1.75rem); font-weight: 800; margin-bottom: 0.4rem;">
          Você tem o perfil de um Homem Inabalável?
        </h2>
        <p id="t-quiz-desc" style="font-size: 0.85rem; color: var(--text-gray);">
          Selecione como você costuma agir nas 3 situações abaixo:
        </p>
      </div>

      <!-- Question 1 -->
      <div class="glass-card" style="margin-bottom: 1rem; padding: 1.25rem;">
        <h4 id="t-q1-title" style="font-size: 0.95rem; font-weight: 700; color: #FFFFFF; margin-bottom: 0.75rem;">
          1. O despertador toca às 05:30 da manhã no frio:
        </h4>
        <div class="quiz-option" onclick="selectQuiz(1, 'weak', this)">
          <span class="radio-circle"></span>
          <span id="t-q1-weak" style="color: #CBD5E1;">Aperto a soneca 3 vezes e fico 30min no feed</span>
        </div>
        <div class="quiz-option" onclick="selectQuiz(1, 'strong', this)">
          <span class="radio-circle"></span>
          <span id="t-q1-strong" style="color: #CBD5E1;">Levanto nos primeiros 5 segundos sem negociar</span>
        </div>
      </div>

      <!-- Question 2 -->
      <div class="glass-card" style="margin-bottom: 1rem; padding: 1.25rem;">
        <h4 id="t-q2-title" style="font-size: 0.95rem; font-weight: 700; color: #FFFFFF; margin-bottom: 0.75rem;">
          2. Quando você recebe uma crítica ou ofensa na internet ou pessoalmente:
        </h4>
        <div class="quiz-option" onclick="selectQuiz(2, 'weak', this)">
          <span class="radio-circle"></span>
          <span id="t-q2-weak" style="color: #CBD5E1;">Fico irritado, respondo na hora e penso nisso o dia todo</span>
        </div>
        <div class="quiz-option" onclick="selectQuiz(2, 'strong', this)">
          <span class="radio-circle"></span>
          <span id="t-q2-strong" style="color: #CBD5E1;">Mantenho a postura estoica; o ruído alheio não me atinge</span>
        </div>
      </div>

      <!-- Question 3 -->
      <div class="glass-card" style="margin-bottom: 1.5rem; padding: 1.25rem;">
        <h4 id="t-q3-title" style="font-size: 0.95rem; font-weight: 700; color: #FFFFFF; margin-bottom: 0.75rem;">
          3. Diante de um trabalho difícil que você precisa entregar:
        </h4>
        <div class="quiz-option" onclick="selectQuiz(3, 'weak', this)">
          <span class="radio-circle"></span>
          <span id="t-q3-weak" style="color: #CBD5E1;">Abro o Instagram/TikTok para 'descansar 5 min' e perco a tarde</span>
        </div>
        <div class="quiz-option" onclick="selectQuiz(3, 'strong', this)">
          <span class="radio-circle"></span>
          <span id="t-q3-strong" style="color: #CBD5E1;">Ativo o modo caverna até a missão estar 100% cumprida</span>
        </div>
      </div>

      <!-- Dynamic Feedback Result -->
      <div id="quizFeedback" style="display: none; background: rgba(245, 158, 11, 0.12); border: 1px solid #F59E0B; border-radius: 1rem; padding: 1.5rem; text-align: center; animation: fadeIn 0.4s ease;">
        <h3 id="t-quiz-feedback-title" style="font-size: 1.05rem; font-weight: 800; color: #F59E0B; margin-bottom: 0.5rem;">
          ⚠️ DIAGNÓSTICO: Você está operando com vazamento de disciplina.
        </h3>
        <p id="t-quiz-feedback-desc" style="font-size: 0.85rem; color: #CBD5E1; margin-bottom: 1.25rem;">
          Se você marcou pelo menos 1 opção fraca, sua mente está no comando dos seus impulsos, e não você. O guia Mente Inabalável foi desenhado exatamente para reprogramar esses padrões.
        </p>
        <a id="t-quiz-feedback-btn-link" href="https://pay.hotmart.com/B107479792A" target="_blank" class="btn-gold" style="padding: 0.85rem 1.5rem; font-size: 0.9rem;">
          <span id="t-quiz-feedback-btn">DESBLOQUEAR O CÓDIGO (R$ 19,90)</span>
        </a>
      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 4. WHAT IS INSIDE (CHAPTERS & CURRICULUM) -->
  <!-- ========================================================================= -->
  <section style="padding: 3.5rem 0;">
    <div class="container-custom">
      
      <div style="text-align: center; margin-bottom: 2rem;">
        <div class="badge-pill badge-gold" style="margin-bottom: 0.6rem;">
          <span id="t-features-badge">CONTEÚDO PROGRAMÁTICO COMPLETO</span>
        </div>
        <h2 id="t-features-title" style="font-size: clamp(1.4rem, 4vw, 1.95rem); font-weight: 800; margin-bottom: 0.4rem;">
          O que você vai dominar dentro do livro:
        </h2>
        <p id="t-features-desc" style="font-size: 0.85rem; color: var(--text-gray);">
          Um roteiro direto ao ponto, sem enrolação teórica ou clichês vazios de autoajuda.
        </p>
      </div>

      <div style="display: flex; flex-direction: column; gap: 0.85rem;">
        
        <!-- Cap 1 -->
        <div class="glass-card" style="display: flex; gap: 1rem; align-items: flex-start; padding: 1.15rem;">
          <div style="background: rgba(245, 158, 11, 0.15); color: #F59E0B; font-weight: 900; font-size: 0.9rem; width: 34px; height: 34px; border-radius: 0.5rem; display: flex; align-items: center; justify-content: center; flex-shrink: 0; border: 1px solid rgba(245, 158, 11, 0.3);">
            01
          </div>
          <div>
            <h4 id="t-f1-title" style="font-size: 0.95rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.25rem;">
              Capítulo 1: O Despertar da Consciência
            </h4>
            <p id="t-f1-desc" style="font-size: 0.82rem; color: var(--text-gray); line-height: 1.5;">
              Como identificar as mentiras sutis que você conta para si mesmo todos os dias e desmascarar a autoilusão.
            </p>
          </div>
        </div>

        <!-- Cap 2 -->
        <div class="glass-card" style="display: flex; gap: 1rem; align-items: flex-start; padding: 1.15rem;">
          <div style="background: rgba(245, 158, 11, 0.15); color: #F59E0B; font-weight: 900; font-size: 0.9rem; width: 34px; height: 34px; border-radius: 0.5rem; display: flex; align-items: center; justify-content: center; flex-shrink: 0; border: 1px solid rgba(245, 158, 11, 0.3);">
            02
          </div>
          <div>
            <h4 id="t-f2-title" style="font-size: 0.95rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.25rem;">
              Capítulo 2: O Fim da Negociação Interna
            </h4>
            <p id="t-f2-desc" style="font-size: 0.82rem; color: var(--text-gray); line-height: 1.5;">
              A Regra dos 5 Segundos aplicada ao estoicismo para agir instantaneamente antes do cérebro sabotar.
            </p>
          </div>
        </div>

        <!-- Cap 3 -->
        <div class="glass-card" style="display: flex; gap: 1rem; align-items: flex-start; padding: 1.15rem;">
          <div style="background: rgba(245, 158, 11, 0.15); color: #F59E0B; font-weight: 900; font-size: 0.9rem; width: 34px; height: 34px; border-radius: 0.5rem; display: flex; align-items: center; justify-content: center; flex-shrink: 0; border: 1px solid rgba(245, 158, 11, 0.3);">
            03
          </div>
          <div>
            <h4 id="t-f3-title" style="font-size: 0.95rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.25rem;">
              Capítulo 3: Blindagem contra o Ruído Externo
            </h4>
            <p id="t-f3-desc" style="font-size: 0.82rem; color: var(--text-gray); line-height: 1.5;">
              Técnicas milenares de Marco Aurélio para neutralizar fofocas, críticas destrutivas e a necessidade de validação social.
            </p>
          </div>
        </div>

        <!-- Cap 4 -->
        <div class="glass-card" style="display: flex; gap: 1rem; align-items: flex-start; padding: 1.15rem;">
          <div style="background: rgba(245, 158, 11, 0.15); color: #F59E0B; font-weight: 900; font-size: 0.9rem; width: 34px; height: 34px; border-radius: 0.5rem; display: flex; align-items: center; justify-content: center; flex-shrink: 0; border: 1px solid rgba(245, 158, 11, 0.3);">
            04
          </div>
          <div>
            <h4 id="t-f4-title" style="font-size: 0.95rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.25rem;">
              Capítulo 4: O Poder do Silêncio e da Postura
            </h4>
            <p id="t-f4-desc" style="font-size: 0.82rem; color: var(--text-gray); line-height: 1.5;">
              Por que falar menos gera mais respeito magnético e autoridade natural em qualquer ambiente social.
            </p>
          </div>
        </div>

        <!-- Cap 5 -->
        <div class="glass-card" style="display: flex; gap: 1rem; align-items: flex-start; padding: 1.15rem;">
          <div style="background: rgba(245, 158, 11, 0.15); color: #F59E0B; font-weight: 900; font-size: 0.9rem; width: 34px; height: 34px; border-radius: 0.5rem; display: flex; align-items: center; justify-content: center; flex-shrink: 0; border: 1px solid rgba(245, 158, 11, 0.3);">
            05
          </div>
          <div>
            <h4 id="t-f5-title" style="font-size: 0.95rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.25rem;">
              Capítulo 5: Foco Cirúrgico na Era da Distração
            </h4>
            <p id="t-f5-desc" style="font-size: 0.82rem; color: var(--text-gray); line-height: 1.5;">
              Como vencer a guerra da dopamina e recuperar 3 a 5 horas diárias que você perde nas redes sociais.
            </p>
          </div>
        </div>

        <!-- Cap 6 -->
        <div class="glass-card" style="display: flex; gap: 1rem; align-items: flex-start; padding: 1.15rem; border: 1px solid rgba(245, 158, 11, 0.4); background: #131826;">
          <div style="background: #F59E0B; color: #000; font-weight: 900; font-size: 0.9rem; width: 34px; height: 34px; border-radius: 0.5rem; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
            06
          </div>
          <div>
            <h4 id="t-f6-title" style="font-size: 0.95rem; font-weight: 800; color: #F59E0B; margin-bottom: 0.25rem;">
              Capítulo 6: O Código do Homem Implacável
            </h4>
            <p id="t-f6-desc" style="font-size: 0.82rem; color: #CBD5E1; line-height: 1.5;">
              O conjunto de 10 princípios inegociáveis para reger seu caráter, suas decisões financeiras e seus relacionamentos.
            </p>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 5. AUTHORITY & PROFILE PROOF -->
  <!-- ========================================================================= -->
  <section style="padding: 3rem 0; background: #0A0D15; border-top: 1px solid var(--border-dark); border-bottom: 1px solid var(--border-dark);">
    <div class="container-custom">
      
      <div style="text-align: center; margin-bottom: 1.75rem;">
        <div class="badge-pill badge-gold" style="margin-bottom: 0.6rem;">
          <span id="t-auth-badge">CONHEÇA O PROJETO</span>
        </div>
        <h2 style="font-size: clamp(1.35rem, 3.8vw, 1.8rem); font-weight: 800; margin-bottom: 0.4rem;">
          <span id="t-auth-title">Construído nos bastidores do</span><br>
          <span id="t-auth-title-gold" class="gold-gradient-text">Perfil Mente Inabalável</span>
        </h2>
        <p id="t-auth-desc" style="font-size: 0.85rem; color: var(--text-gray); max-width: 520px; margin: 0 auto;">
          Uma comunidade dedicada ao resgate da masculinidade sólida, foco de ferro e desenvolvimento pessoal prático.
        </p>
      </div>

      <div class="glass-card" style="padding: 1.5rem; text-align: left;">
        <div style="display: flex; flex-direction: column; gap: 0.85rem;">
          
          <div style="display: flex; align-items: flex-start; gap: 0.75rem;">
            <span style="color: #F59E0B; font-size: 1.1rem; line-height: 1;">✓</span>
            <p id="t-auth1" style="font-size: 0.88rem; color: #CBD5E1; line-height: 1.5;">
              Mais de 100 mil homens impactados diariamente por nossas pílulas de sabedoria estoica e disciplina.
            </p>
          </div>

          <div style="display: flex; align-items: flex-start; gap: 0.75rem;">
            <span style="color: #F59E0B; font-size: 1.1rem; line-height: 1;">✓</span>
            <p id="t-auth2" style="font-size: 0.88rem; color: #CBD5E1; line-height: 1.5;">
              Metodologia testada e validada em centenas de leitores reais que transformaram sua rotina e postura.
            </p>
          </div>

          <div style="display: flex; align-items: flex-start; gap: 0.75rem;">
            <span style="color: #F59E0B; font-size: 1.1rem; line-height: 1;">✓</span>
            <p id="t-auth3" style="font-size: 0.88rem; color: #CBD5E1; line-height: 1.5;">
              Sem enrolação, sem teorias complexas: direto ao ponto com protocolos aplicáveis no seu dia a dia.
            </p>
          </div>

        </div>

        <div style="margin-top: 1.25rem; padding-top: 1rem; border-top: 1px solid rgba(255, 255, 255, 0.08); text-align: center;">
          <p id="t-auth-footer" style="font-size: 0.78rem; color: #F59E0B; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em;">
            Nosso lema: Menos desculpas, mais postura. Menos falação, mais resultados.
          </p>
        </div>
      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 6. THE COMPLETE OFFER BUNDLE + PRICING -->
  <!-- ========================================================================= -->
  <section id="oferta" style="padding: 4rem 0; position: relative;">
    <div class="container-custom">
      
      <div style="text-align: center; margin-bottom: 2rem;">
        <div class="badge-pill badge-green" style="margin-bottom: 0.6rem;">
          <span id="t-offer-badge">OFERTA COMPLETA DE LANÇAMENTO</span>
        </div>
        <h2 id="t-offer-title" style="font-size: clamp(1.5rem, 4.2vw, 2.15rem); font-weight: 900; margin-bottom: 0.4rem;">
          Tudo o que você vai receber hoje:
        </h2>
        <p id="t-offer-desc" style="font-size: 0.88rem; color: var(--text-gray);">
          Adquirindo agora na Hotmart, você leva o livro principal + 2 bônus práticos exclusivos sem custo extra.
        </p>
      </div>

      <!-- Main Offer Box -->
      <div class="glass-card" style="border: 2px solid #F59E0B; position: relative; padding: 2rem 1.5rem; box-shadow: 0 15px 35px -5px rgba(245, 158, 11, 0.25);">
        
        <div style="position: absolute; top: -14px; left: 50%; transform: translateX(-50%); background: #F59E0B; color: #000; font-size: 0.72rem; font-weight: 900; letter-spacing: 0.08em; text-transform: uppercase; padding: 0.3rem 1rem; border-radius: 2rem; white-space: nowrap;">
          <span id="t-offer-card-tag">PACOTE COMPLETO DE TRANSFORMAÇÃO</span>
        </div>

        <!-- Bundle Visual Graphic -->
        <div style="text-align: center; margin-bottom: 1.5rem;">
          <img src="{b64_bundle}" alt="Combo Completo Mente Inabalável + Bônus" style="width: 100%; max-width: 320px; height: auto; border-radius: 10px; filter: drop-shadow(0 15px 25px rgba(0,0,0,0.6));">
        </div>

        <!-- Items Breakdown -->
        <div style="display: flex; flex-direction: column; gap: 1rem; margin-bottom: 1.75rem;">
          
          <!-- Item 1: Main Book -->
          <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 0.75rem; padding: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.25rem;">
              <strong id="t-item1-title" style="font-size: 0.95rem; color: #FFFFFF;">1. Livro Digital Oficial: Mente Inabalável (PDF)</strong>
              <span id="t-price-ebook" style="color: #94A3B8; text-decoration: line-through; font-size: 0.85rem; font-weight: 600;">R$ 67,00</span>
            </div>
            <p id="t-item1-desc" style="font-size: 0.78rem; color: #94A3B8;">
              O manual completo de 34 páginas com os 6 capítulos fundamentais, exercícios práticos e o código dos 10 princípios inegociáveis.
            </p>
          </div>

          <!-- Item 2: Bonus 1 -->
          <div style="background: rgba(245, 158, 11, 0.05); border: 1px solid rgba(245, 158, 11, 0.2); border-radius: 0.75rem; padding: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.25rem;">
              <div>
                <span id="t-item2-badge" class="badge-pill badge-gold" style="font-size: 0.65rem; padding: 0.15rem 0.5rem; margin-bottom: 0.25rem;">BÔNUS 1 • EXCLUSIVO</span>
                <strong id="t-item2-title" style="font-size: 0.95rem; color: #FFFFFF; display: block;">2. Protocolo de 21 Dias de Desafio Prático</strong>
              </div>
              <div style="text-align: right;">
                <span id="t-price-b1" style="color: #64748B; text-decoration: line-through; font-size: 0.8rem; display: block;">R$ 40,00</span>
                <span style="color: #10B981; font-weight: 800; font-size: 0.85rem;">GRÁTIS</span>
              </div>
            </div>
            <p id="t-item2-desc" style="font-size: 0.78rem; color: #94A3B8;">
              Um plano passo a passo com uma tarefa diária específica para implementar a blindagem mental na sua rotina e quebrar a inércia.
            </p>
          </div>

          <!-- Item 3: Bonus 2 -->
          <div style="background: rgba(245, 158, 11, 0.05); border: 1px solid rgba(245, 158, 11, 0.2); border-radius: 0.75rem; padding: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.25rem;">
              <div>
                <span id="t-item3-badge" class="badge-pill badge-gold" style="font-size: 0.65rem; padding: 0.15rem 0.5rem; margin-bottom: 0.25rem;">BÔNUS 2 • EXCLUSIVO</span>
                <strong id="t-item3-title" style="font-size: 0.95rem; color: #FFFFFF; display: block;">3. Checklist Diário do Homem Focado</strong>
              </div>
              <div style="text-align: right;">
                <span id="t-price-b2" style="color: #64748B; text-decoration: line-through; font-size: 0.8rem; display: block;">R$ 40,00</span>
                <span style="color: #10B981; font-weight: 800; font-size: 0.85rem;">GRÁTIS</span>
              </div>
            </div>
            <p id="t-item3-desc" style="font-size: 0.78rem; color: #94A3B8;">
              A ferramenta de acompanhamento rápido para imprimir ou salvar no celular e auditar sua consistência diária em 2 minutos.
            </p>
          </div>

        </div>

        <!-- Pricing Summary Box -->
        <div style="border-top: 1px solid rgba(255, 255, 255, 0.1); padding-top: 1.25rem; text-align: center; margin-bottom: 1.5rem;">
          <p style="font-size: 0.85rem; color: #64748B; margin-bottom: 0.25rem;">
            <span id="t-total-val-label">Valor Total de Mercado:</span> <span id="t-price-total" style="text-decoration: line-through; color: #94A3B8; font-weight: 700;">R$ 147,00</span>
          </p>
          <div style="margin-bottom: 0.5rem;">
            <span id="t-promo-price-label" style="font-size: 0.9rem; color: #CBD5E1; display: block;">Valor Promocional de Lançamento:</span>
            <span id="t-price-big" style="font-size: 2.85rem; font-weight: 900; color: #F59E0B; line-height: 1;">R$ 19,90</span>
          </div>
          <p id="t-payment-type-label" style="font-size: 0.75rem; color: #10B981; font-weight: 600;">
            Pagamento único • Acesso vitalício • Sem mensalidades
          </p>
        </div>

        <!-- Hotmart Official CTA Button -->
        <a id="t-cta-offer-btn" href="https://pay.hotmart.com/B107479792A" target="_blank" class="btn-gold pulse-glow" style="margin-bottom: 0.75rem;">
          <span id="t-cta-offer">ATIVAR MEU CÓDIGO AGORA (R$ 19,90)</span>
          <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/>
          </svg>
        </a>

        <div style="text-align: center; font-size: 0.72rem; color: #94A3B8;">
          <span id="t-secure-proc">🔒 Processamento Oficial Seguro via Hotmart • Acesso Imediato</span>
          <div id="t-payment-methods" style="margin-top: 0.35rem; color: #CBD5E1; font-weight: 600;">
            ⚡ PIX Instantâneo • 💳 Cartão de Crédito • 📄 Boleto
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 7. WHO IS IT FOR / WHO IS IT NOT FOR -->
  <!-- ========================================================================= -->
  <section style="padding: 3rem 0; background: #0A0D15; border-top: 1px solid var(--border-dark); border-bottom: 1px solid var(--border-dark);">
    <div class="container-custom">
      
      <!-- Device Compatibility Box -->
      <div style="background: rgba(245, 158, 11, 0.08); border: 1px solid rgba(245, 158, 11, 0.25); border-radius: 1rem; padding: 1.25rem; text-align: center; margin-bottom: 2.5rem;">
        <h4 id="t-compat-title" style="font-size: 1rem; font-weight: 800; color: #F59E0B; margin-bottom: 0.35rem;">
          📱 Formato 100% Digital e Acessível
        </h4>
        <p id="t-compat-desc" style="font-size: 0.82rem; color: #CBD5E1; line-height: 1.5;">
          Receba o material instantaneamente no seu e-mail após a aprovação da compra na Hotmart. Leia no smartphone (iOS/Android), tablet, Kindle ou computador. O arquivo é seu para sempre.
        </p>
      </div>

      <div style="display: grid; grid-template-columns: 1fr; gap: 1.5rem;">
        
        <!-- Not For -->
        <div class="glass-card" style="border-left: 3px solid #EF4444;">
          <h3 id="t-not-for-title" style="font-size: 1.05rem; font-weight: 800; color: #EF4444; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
            <span>✕</span> Para quem NÃO é este guia:
          </h3>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.5rem; font-size: 0.85rem; color: #94A3B8;">
            <li id="t-not-for-1" style="display: flex; gap: 0.5rem; align-items: flex-start;">
              <span style="color: #EF4444;">•</span> Pessoas que buscam fórmulas mágicas de sucesso sem fazer esforço diário.
            </li>
            <li id="t-not-for-2" style="display: flex; gap: 0.5rem; align-items: flex-start;">
              <span style="color: #EF4444;">•</span> Quem prefere continuar reclamando das circunstâncias e culpando o mundo.
            </li>
            <li id="t-not-for-3" style="display: flex; gap: 0.5rem; align-items: flex-start;">
              <span style="color: #EF4444;">•</span> Quem se ofende facilmente com verdades duras e autocrítica necessária.
            </li>
          </ul>
        </div>

        <!-- For -->
        <div class="glass-card" style="border-left: 3px solid #10B981;">
          <h3 id="t-for-title" style="font-size: 1.05rem; font-weight: 800; color: #10B981; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
            <span>✓</span> Para quem É este guia:
          </h3>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.5rem; font-size: 0.85rem; color: #CBD5E1;">
            <li id="t-for-1" style="display: flex; gap: 0.5rem; align-items: flex-start;">
              <span style="color: #10B981;">✓</span> Quem cansou de prometer mudanças para si mesmo e falhar no dia seguinte.
            </li>
            <li id="t-for-2" style="display: flex; gap: 0.5rem; align-items: flex-start;">
              <span style="color: #10B981;">✓</span> Quem deseja dominar suas emoções, parar de procrastinar e ter foco absoluto.
            </li>
            <li id="t-for-3" style="display: flex; gap: 0.5rem; align-items: flex-start;">
              <span style="color: #10B981;">✓</span> Homens que querem construir uma reputação de respeito, honra e solidez.
            </li>
          </ul>
        </div>

      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 8. 7-DAY GUARANTEE -->
  <!-- ========================================================================= -->
  <section style="padding: 3.5rem 0;">
    <div class="container-custom">
      <div class="glass-card" style="border: 1px solid rgba(16, 185, 129, 0.4); background: rgba(16, 185, 129, 0.04); text-align: center; padding: 2rem 1.5rem;">
        <div style="font-size: 2.75rem; margin-bottom: 0.75rem;">🛡️</div>
        <div class="badge-pill badge-green" style="margin-bottom: 0.6rem;">
          <span id="t-guar-badge">RISCO ZERO ABSOLUTO</span>
        </div>
        <h2 id="t-guar-title" style="font-size: 1.45rem; font-weight: 800; margin-bottom: 0.75rem; color: #FFFFFF;">
          7 Dias de Garantia Incondicional Hotmart
        </h2>
        <p id="t-guar-desc" style="font-size: 0.88rem; color: var(--text-gray); line-height: 1.6; max-width: 520px; margin: 0 auto 1rem auto;">
          Leia o material, aplique o Protocolo de 21 Dias e sinta a mudança na sua mente. Se por qualquer motivo você achar que o conteúdo não agregou valor brutal na sua vida, basta solicitar o reembolso na Hotmart com um clique. Devolvemos 100% do seu dinheiro.
        </p>
        <p id="t-guar-bold" style="font-size: 0.8rem; color: #10B981; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em;">
          Sem perguntas, sem burocracia e sem ressentimentos. O risco é todo meu.
        </p>
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 9. FAQ ACCORDION -->
  <!-- ========================================================================= -->
  <section style="padding: 3rem 0; background: #0A0D15; border-top: 1px solid var(--border-dark); border-bottom: 1px solid var(--border-dark);">
    <div class="container-custom">
      
      <div style="text-align: center; margin-bottom: 2rem;">
        <div class="badge-pill badge-gold" style="margin-bottom: 0.6rem;">
          <span id="t-faq-badge">TIRE SUAS DÚVIDAS</span>
        </div>
        <h2 id="t-faq-title" style="font-size: clamp(1.4rem, 4vw, 1.85rem); font-weight: 800;">
          Perguntas Frequentes
        </h2>
      </div>

      <div>
        <details open>
          <summary id="t-faq1-q">Como vou receber o material após a compra?</summary>
          <div id="t-faq1-a" class="faq-answer">
            Assim que a compra for confirmada pela Hotmart (instantâneo no PIX e Cartão), você receberá um e-mail com o link direto para download do e-book em PDF de alta resolução e de todos os bônus inclusos.
          </div>
        </details>

        <details>
          <summary id="t-faq2-q">Quais são as formas de pagamento disponíveis?</summary>
          <div id="t-faq2-a" class="faq-answer">
            Você pode pagar com total segurança e garantia via PIX (aprovação imediata), Cartão de Crédito ou Boleto bancário diretamente na Hotmart por apenas R$ 19,90.
          </div>
        </details>

        <details>
          <summary id="t-faq3-q">O e-book funciona no meu celular?</summary>
          <div id="t-faq3-a" class="faq-answer">
            Sim! O livro digital foi diagramado e otimizado para leitura fluida tanto em celulares (iOS/Android) quanto em tablets, computadores e leitores digitais como Kindle.
          </div>
        </details>

        <details>
          <summary id="t-faq4-q">E se eu não gostar do conteúdo?</summary>
          <div id="t-faq4-a" class="faq-answer">
            Você está 100% protegido pela garantia incondicional de 7 dias da Hotmart. Basta pedir reembolso na plataforma e seu investimento será devolvido integralmente.
          </div>
        </details>

        <details>
          <summary id="t-faq5-q">Eu terei que pagar mensalidade?</summary>
          <div id="t-faq5-a" class="faq-answer">
            Não! O pagamento de R$ 19,90 é único e o acesso ao material é vitalício.
          </div>
        </details>
      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 10. FINAL CALL TO ACTION (BOTTOM) -->
  <!-- ========================================================================= -->
  <section style="padding: 4.5rem 0 6rem 0; text-align: center; position: relative;">
    <div class="container-custom">
      
      <h2 style="font-size: clamp(1.6rem, 4.8vw, 2.35rem); font-weight: 900; line-height: 1.2; margin-bottom: 1rem; text-transform: uppercase;">
        <span id="t-final-title">A decisão que define o seu futuro</span><br>
        <span id="t-final-title-gold" class="gold-gradient-text">é tomada AGORA.</span>
      </h2>
      
      <p id="t-final-desc" style="font-size: 0.95rem; color: var(--text-gray); max-width: 540px; margin: 0 auto 2rem auto; line-height: 1.6;">
        Enquanto você adia, a sua vida passa. Você pode continuar no mesmo ciclo de desculpas, ou investir <strong style='color:#F59E0B'>R$ 19,90</strong> agora na Hotmart e ativar o código que vai blindar a sua mente.
      </p>

      <a id="t-final-cta-btn" href="https://pay.hotmart.com/B107479792A" target="_blank" class="btn-gold pulse-glow" style="max-width: 480px; margin: 0 auto 1.5rem auto;">
        <span id="t-final-cta">SIM! QUERO SER UM HOMEM INABALÁVEL</span>
        <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/>
        </svg>
      </a>

      <p id="t-final-urgency" style="font-size: 0.78rem; color: #F59E0B; font-weight: 700;">
        ⚡ Oferta por tempo limitado. O valor pode retornar para R$ 97,00 a qualquer momento.
      </p>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- FOOTER -->
  <!-- ========================================================================= -->
  <footer style="background: #040508; border-top: 1px solid var(--border-dark); padding: 2.5rem 1rem 6.5rem 1rem; text-align: center; font-size: 0.75rem; color: #64748B;">
    <div class="container-custom">
      <div style="font-weight: 800; font-size: 0.95rem; color: #FFFFFF; margin-bottom: 0.5rem; letter-spacing: 0.05em;">
        MENTE INABALÁVEL™
      </div>
      <p style="margin-bottom: 0.75rem;">
        Todos os direitos reservados • Processamento oficial via Hotmart
      </p>
      <p style="font-size: 0.68rem; color: #475569; max-width: 480px; margin: 0 auto; line-height: 1.4;">
        Este site não é afiliado ao TikTok, Meta, Facebook ou Google. Todos os resultados dependem da dedicação pessoal e da aplicação consistente dos princípios contidos na obra.
      </p>
    </div>
  </footer>

  <!-- ========================================================================= -->
  <!-- STICKY BOTTOM CONVERSION BAR -->
  <!-- ========================================================================= -->
  <div class="sticky-buy-bar">
    <div style="max-width: 680px; margin: 0 auto; width: 100%; display: flex; align-items: center; justify-content: space-between; gap: 0.75rem;">
      <div style="display: flex; flex-direction: column; text-align: left;">
        <span style="font-size: 0.68rem; color: #94A3B8; text-transform: uppercase; font-weight: 700;">Acesso Vitalício Hotmart</span>
        <span id="t-sticky-price" style="font-size: 1.25rem; font-weight: 900; color: #F59E0B;">R$ 19,90</span>
      </div>
      <a id="t-sticky-btn-link" href="https://pay.hotmart.com/B107479792A" target="_blank" class="btn-gold" style="padding: 0.75rem 1.15rem; font-size: 0.8rem; border-radius: 0.75rem; width: auto; flex: 1;">
        <span id="t-sticky-btn">COMPRAR NA HOTMART (R$ 19,90)</span>
      </a>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- JAVASCRIPT LOGIC & REACTIVE TRANSLATIONS -->
  <!-- ========================================================================= -->
  <script>
    const i18n = TRANSLATIONS_JSON_PLACEHOLDER;
    let currentCountry = 'BR';

    function setContent(id, html) {{
      const el = document.getElementById(id);
      if (el) el.innerHTML = html;
    }}

    function selectCountry(countryCode) {{
      if (!i18n[countryCode]) return;
      currentCountry = countryCode;
      localStorage.setItem('user_country_choice', countryCode);
      document.getElementById('countryModal').style.display = 'none';

      // Update Header Switcher active state
      ['BR', 'US', 'ES'].forEach(c => {{
        const btn = document.getElementById('btn-' + c);
        if (btn) {{
          if (c === countryCode) btn.classList.add('active');
          else btn.classList.remove('active');
        }}
      }});

      const d = i18n[countryCode];

      // Update text fields
      document.documentElement.lang = d.lang_code;
      setContent('t-scarcity', '• ' + d.scarcity_text);
      setContent('t-hook-badge', d.hook_badge);
      setContent('t-headline-start', d.headline_start);
      setContent('t-headline-highlight', d.headline_highlight);
      setContent('t-headline-end', d.headline_end);
      setContent('t-subheadline', d.subheadline);
      setContent('t-image-badge', d.image_badge);
      setContent('t-price-anchor', 'De ' + d.price_anchor);
      setContent('t-price-current', 'Por apenas ' + d.price_current);
      setContent('t-cta-hero', d.cta_hero);

      setContent('t-trust-secure', d.trust_secure);
      setContent('t-trust-instant', d.trust_instant);
      setContent('t-trust-guarantee', d.trust_guarantee);

      setContent('t-problem-badge', d.problem_badge);
      setContent('t-problem-title', d.problem_title);
      setContent('t-problem-title-red', d.problem_title_red);
      setContent('t-problem-p1', d.problem_p1);
      setContent('t-problem-p2', d.problem_p2);
      setContent('t-problem-p3', d.problem_p3);
      setContent('t-problem-quote', d.problem_quote);

      setContent('t-turn-badge', d.turn_badge);
      setContent('t-turn-title', d.turn_title);
      setContent('t-turn-title-gold', d.turn_title_gold);
      setContent('t-turn-p1', d.turn_p1);
      setContent('t-turn-p2', d.turn_p2);
      setContent('t-turn-p3', d.turn_p3);
      setContent('t-pillar1-title', d.pillar1_title);
      setContent('t-pillar1-desc', d.pillar1_desc);
      setContent('t-pillar2-title', d.pillar2_title);
      setContent('t-pillar2-desc', d.pillar2_desc);

      setContent('t-quiz-badge', d.quiz_badge);
      setContent('t-quiz-title', d.quiz_title);
      setContent('t-quiz-desc', d.quiz_desc);
      setContent('t-q1-title', d.q1_title);
      setContent('t-q1-weak', d.q1_weak);
      setContent('t-q1-strong', d.q1_strong);
      setContent('t-q2-title', d.q2_title);
      setContent('t-q2-weak', d.q2_weak);
      setContent('t-q2-strong', d.q2_strong);
      setContent('t-q3-title', d.q3_title);
      setContent('t-q3-weak', d.q3_weak);
      setContent('t-q3-strong', d.q3_strong);
      setContent('t-quiz-feedback-title', d.quiz_feedback_title);
      setContent('t-quiz-feedback-desc', d.quiz_feedback_desc);
      setContent('t-quiz-feedback-btn', d.quiz_feedback_btn);

      setContent('t-features-badge', d.features_badge);
      setContent('t-features-title', d.features_title);
      setContent('t-features-desc', d.features_desc);
      setContent('t-f1-title', d.f1_title);
      setContent('t-f1-desc', d.f1_desc);
      setContent('t-f2-title', d.f2_title);
      setContent('t-f2-desc', d.f2_desc);
      setContent('t-f3-title', d.f3_title);
      setContent('t-f3-desc', d.f3_desc);
      setContent('t-f4-title', d.f4_title);
      setContent('t-f4-desc', d.f4_desc);
      setContent('t-f5-title', d.f5_title);
      setContent('t-f5-desc', d.f5_desc);
      setContent('t-f6-title', d.f6_title);
      setContent('t-f6-desc', d.f6_desc);

      setContent('t-auth-badge', d.auth_badge);
      setContent('t-auth-title', d.auth_title);
      setContent('t-auth-title-gold', d.auth_title_gold);
      setContent('t-auth-desc', d.auth_desc);
      setContent('t-auth1', d.auth1);
      setContent('t-auth2', d.auth2);
      setContent('t-auth3', d.auth3);
      setContent('t-auth-footer', d.auth_footer);

      setContent('t-offer-badge', d.offer_badge);
      setContent('t-offer-title', d.offer_title);
      setContent('t-offer-desc', d.offer_desc);
      setContent('t-offer-card-tag', d.offer_card_tag);
      setContent('t-item1-title', d.item1_title);
      setContent('t-item1-desc', d.item1_desc);
      setContent('t-item2-badge', d.item2_badge);
      setContent('t-item2-title', d.item2_title);
      setContent('t-item2-desc', d.item2_desc);
      setContent('t-item3-badge', d.item3_badge);
      setContent('t-item3-title', d.item3_title);
      setContent('t-item3-desc', d.item3_desc);
      setContent('t-price-ebook', d.price_ebook);
      setContent('t-price-b1', d.price_b1);
      setContent('t-price-b2', d.price_b2);
      setContent('t-price-total', d.price_total);
      setContent('t-total-val-label', d.total_val_label);
      setContent('t-promo-price-label', d.promo_price_label);
      setContent('t-price-big', d.price_current);
      setContent('t-payment-type-label', d.payment_type_label);
      setContent('t-cta-offer', d.cta_offer);
      setContent('t-secure-proc', d.secure_proc);
      setContent('t-payment-methods', d.payment_methods);

      setContent('t-compat-title', d.compat_title);
      setContent('t-compat-desc', d.compat_desc);
      setContent('t-not-for-title', d.not_for_title);
      setContent('t-not-for-1', d.not_for_1);
      setContent('t-not-for-2', d.not_for_2);
      setContent('t-not-for-3', d.not_for_3);
      setContent('t-for-title', d.for_title);
      setContent('t-for-1', d.for_1);
      setContent('t-for-2', d.for_2);
      setContent('t-for-3', d.for_3);

      setContent('t-guar-badge', d.guar_badge);
      setContent('t-guar-title', d.guar_title);
      setContent('t-guar-desc', d.guar_desc);
      setContent('t-guar-bold', d.guar_bold);

      setContent('t-final-title', d.final_title);
      setContent('t-final-title-gold', d.final_title_gold);
      setContent('t-final-desc', d.final_desc);
      setContent('t-final-cta', d.final_cta);
      setContent('t-final-urgency', d.final_urgency);

      setContent('t-faq-badge', d.faq_badge);
      setContent('t-faq-title', d.faq_title);
      setContent('t-faq1-q', d.faq1_q);
      setContent('t-faq1-a', d.faq1_a);
      setContent('t-faq2-q', d.faq2_q);
      setContent('t-faq2-a', d.faq2_a);
      setContent('t-faq3-q', d.faq3_q);
      setContent('t-faq3-a', d.faq3_a);
      setContent('t-faq4-q', d.faq4_q);
      setContent('t-faq4-a', d.faq4_a);
      setContent('t-faq5-q', d.faq5_q);
      setContent('t-faq5-a', d.faq5_a);

      setContent('t-sticky-price', d.price_current);
      setContent('t-sticky-btn', d.sticky_btn);

      // Update URLs for CTA buttons
      document.getElementById('t-cta-hero-btn').href = d.checkout_url;
      document.getElementById('t-cta-offer-btn').href = d.checkout_url;
      document.getElementById('t-final-cta-btn').href = d.checkout_url;
      document.getElementById('t-sticky-btn-link').href = d.checkout_url;
      document.getElementById('t-quiz-feedback-btn-link').href = d.checkout_url;
    }}

    // Initialize country from storage or detect browser language
    window.addEventListener('DOMContentLoaded', () => {{
      const saved = localStorage.getItem('user_country_choice');
      if (saved && i18n[saved]) {{
        selectCountry(saved);
      }} else {{
        // Detect browser language
        const navLang = (navigator.language || navigator.userLanguage || '').toLowerCase();
        let detected = 'BR';
        if (navLang.startsWith('es')) detected = 'ES';
        else if (navLang.startsWith('en')) detected = 'US';
        else if (navLang.startsWith('pt')) detected = 'BR';

        selectCountry(detected);
        // Show modal selector on first visit so user can easily confirm/change
        document.getElementById('countryModal').style.display = 'flex';
      }}
    }});

    // Countdown Timer
    let totalSeconds = 14 * 60 + 59;
    const countdownEl = document.getElementById('countdown');
    function updateCountdown() {{
      const minutes = Math.floor(totalSeconds / 60);
      const seconds = totalSeconds % 60;
      countdownEl.textContent = `${{String(minutes).padStart(2, '0')}}:${{String(seconds).padStart(2, '0')}}`;
      if (totalSeconds > 0) totalSeconds--;
      else totalSeconds = 15 * 60;
    }}
    setInterval(updateCountdown, 1000);
    updateCountdown();

    // Quiz Logic
    const quizState = {{ 1: null, 2: null, 3: null }};
    function selectQuiz(qNum, choice, el) {{
      const parent = el.parentElement;
      const options = parent.querySelectorAll('.quiz-option');
      options.forEach(opt => {{
        opt.classList.remove('selected-weak', 'selected-strong');
        const circle = opt.querySelector('.radio-circle');
        circle.textContent = '';
        circle.style.borderColor = '#475569';
        circle.style.background = 'transparent';
      }});

      const circle = el.querySelector('.radio-circle');
      if (choice === 'weak') {{
        el.classList.add('selected-weak');
        circle.textContent = '✕';
        circle.style.borderColor = '#EF4444';
        circle.style.background = '#EF4444';
        circle.style.color = '#FFFFFF';
      }} else {{
        el.classList.add('selected-strong');
        circle.textContent = '✓';
        circle.style.borderColor = '#F59E0B';
        circle.style.background = '#F59E0B';
        circle.style.color = '#07080B';
      }}

      quizState[qNum] = choice;
      if (quizState[1] && quizState[2] && quizState[3]) {{
        const feedback = document.getElementById('quizFeedback');
        feedback.style.display = 'block';
      }}
    }}
  </script>

</body>
</html>"""

# Inject JSON
json_str = json.dumps(translations, ensure_ascii=False)
final_html = html_template.replace("TRANSLATIONS_JSON_PLACEHOLDER", json_str)

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Successfully generated Hotmart-exclusive Sales Page (BR, US, ES)! Size:", os.path.getsize('/home/user/index.html'))
