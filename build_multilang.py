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
    "MZ": {
        "lang_code": "pt-MZ",
        "country_name": "Moçambique",
        "flag": "🇲🇿",
        "currency_symbol": "MT",
        "price_anchor": "597MT",
        "price_total": "647MT",
        "price_current": "147MT",
        "price_ebook": "397MT",
        "price_b1": "150MT",
        "price_b2": "100MT",
        "checkout_url": "https://checkout.escalepay.com/1889386",
        "checkout_platform": "Escale Pay",
        "payment_methods": "🇲🇿 M-Pesa • 🇲🇿 E-Mola • 💳 Cartões",
        "badge_top": "CONDIÇÃO DE LANÇAMENTO NA ESCALE PAY",
        "scarcity_text": "Restam apenas 7 vagas com preço de lançamento",
        "hook_badge": "GUIA OFICIAL DO PERFIL MENTE INABALÁVEL",
        "headline_start": "PARE DE",
        "headline_highlight": "NEGOCIAR COM VOCÊ MESMO",
        "headline_end": "E ASSUMA O CONTROLE.",
        "subheadline": "O sistema estoico e prático para jovens que querem eliminar a procrastinação, dominar as próprias emoções e construir disciplina inabalável em 21 dias.",
        "image_badge": "📦 E-BOOK EM PDF + 2 BÔNUS PRÁTICOS • ENTREGA IMEDIATA",
        "cta_hero": "QUERO ATIVAR MINHA MENTE INABALÁVEL",
        "trust_secure": "Compra 100% Segura via Escale Pay",
        "trust_instant": "Entrega Imediata no E-mail",
        "trust_guarantee": "Garantia de 7 Dias",
        "problem_badge": "A REALIDADE NUA E CRUA",
        "problem_title": "Você já sabe o que fazer.",
        "problem_title_red": "O problema é que você não faz.",
        "problem_p1": "Você não está aqui por falta de informação. Já sabe que precisa acordar no horário. Já sabe que o celular está te comendo vivo. Já sabe exatamente qual vício está te matando devagar.",
        "problem_p2": "À noite, assistindo a um vídeo com trilha épica no TikTok, você promete que <strong style='color:#fff'>'amanhã tudo vai ser diferente'</strong>. Sente aquele arrepio de motivação às 23h.",
        "problem_p3": "Mas às 6h da manhã, o arrepio já morreu. Você aperta a soneca três vezes, acorda arrastado, pega o celular antes de levantar e passa 40 minutos rolando a tela no automático.",
        "problem_quote": "O problema nunca foi falta de vontade. O problema é que você negocia com você mesmo todos os dias. <strong style='color:#F59E0B'>E você sempre perde.</strong>",
        "turn_badge": "A VIRADA DE CHAVE",
        "turn_title": "Motivação é combustível fraco.",
        "turn_title_gold": "O que você precisa é de um motor.",
        "turn_p1": "Te ensinaram que mudança começa com motivação. Isso é uma armadilha. Motivação é emoção. Emoção é clima: muda toda hora. Ninguém constrói um império esperando o dia estar ensolarado.",
        "turn_p2": "O motor não pergunta se você está inspirado. <strong style='color:#fff'>Ele simplesmente liga e executa.</strong>",
        "turn_p3": "O que te falta não é mais um vídeo motivacional. O que te falta é um <strong style='color:#FDE68A'>sistema mental inegociável</strong>: estoicismo aplicado para dominar o que acontece dentro de você, e frieza estratégica para lidar com o que acontece fora.",
        "pillar1_title": "🛡️ ESTOICISMO APLICADO",
        "pillar1_desc": "Para governar impulsos, destruir a ansiedade e controlar a única coisa que realmente depende de você: suas escolhas.",
        "pillar2_title": "⚔️ FRIEZA ESTRATÉGICA",
        "pillar2_desc": "Para agir sem plateia, cortar distrações sem culpa e se tornar ilegível e imune a provocações alheias.",
        "quiz_badge": "⚡ TESTE DO ESPELHO • SEM MEIO-TERMO",
        "quiz_title": "Questionário de Confronto",
        "quiz_desc": "Seja brutalmente sincero consigo mesmo antes de continuar lendo. Marque a sua escolha:",
        "q1_title": "Você quer mudar de verdade ou quer continuar assim?",
        "q1_weak": "Continuar adiando e esperando uma 'motivação mágica' aparecer",
        "q1_strong": "Assumir o controle agora e pagar o preço da disciplina",
        "q2_title": "Depois de mais um dia igual e sem resultado, o que você escolhe?",
        "q2_weak": "Mais um dia de desculpas confortáveis para aliviar a culpa",
        "q2_strong": "Construir hoje o primeiro tijolo de um homem inabalável",
        "q3_title": "Quem decide o seu humor e as suas ações hoje?",
        "q3_weak": "As notificações do celular, o que os outros dizem e o clima",
        "q3_strong": "Eu. Absolutamente nada e ninguém me tira do eixo.",
        "quiz_feedback_title": "Se você marcou a opção do implacável, o próximo passo é este:",
        "quiz_feedback_desc": "A conversa fiada acaba aqui. Chega de viver de promessas não cumpridas. Seu desconto exclusivo de lançamento foi ativado:",
        "quiz_feedback_btn": "DESBLOQUEAR O CÓDIGO (147MT)",
        "features_badge": "CONTEÚDO PRÁTICO",
        "features_title": "O Que Você Vai Dominar na Prática",
        "features_desc": "Ferramentas brutas para você aplicar imediatamente no seu dia a dia:",
        "f1_title": "A Regra dos 6 Segundos",
        "f1_desc": "Como atravessar o pico emocional sem agir, matar discussões inúteis e nunca mais mandar mensagens que você vai se arrepender.",
        "f2_title": "A Morte das Desculpas",
        "f2_desc": "O corte de linguagem cirúrgico: troque 'não deu tempo' por 'não foi prioridade' e veja sua mente parar de inventar desculpas.",
        "f3_title": "Frieza & Silêncio Estratégico",
        "f3_desc": "Por que quem fala primeiro entrega vantagem. Aprenda a executar seus planos em silêncio absoluto até o resultado aparecer.",
        "f4_title": "O Inventário de Drenos",
        "f4_desc": "Como cortar pessoas tóxicas, telas viciantes e hábitos fracos sem briga, sem drama e aplicando atrito inteligente.",
        "f5_title": "A Dicotomia do Controle",
        "f5_desc": "A regra milenar para parar de sofrer por opinião dos outros, trânsito ou passado, investindo 100% de energia nas suas ações.",
        "f6_title": "Seu Código Pessoal",
        "f6_desc": "Como definir no máximo 7 regras inegociáveis com punições reais para nunca mais tomar decisões fracas no calor do momento.",
        "auth_badge": "AUTORIDADE MILENAR",
        "auth_title": "Não é achismo de internet.",
        "auth_title_gold": "É a doutrina dos imperadores.",
        "auth_desc": "Este método não foi inventado em um vídeo passageiro. É a síntese prática dos princípios que mantiveram homens inabaláveis diante de guerras e crises:",
        "auth1": "<strong style='color:#F59E0B'>🏛️ Marco Aurélio:</strong> O imperador de Roma que governava exércitos e treinava a mente todas as noites para não ser controlado pela vaidade.",
        "auth2": "<strong style='color:#F59E0B'>📜 Sêneca:</strong> O conselheiro imperial que provou que a mente fraca sofre mais na imaginação do que na realidade.",
        "auth3": "<strong style='color:#F59E0B'>⚔️ Epicteto:</strong> O homem que nasceu escravo, conquistou a liberdade interior e ensinou que ninguém tem poder sobre a sua mente a menos que você permita.",
        "auth_footer": "Traduzido de forma cirúrgica para o jovem de hoje: foco, telas, vícios e disciplina de aço.",
        "offer_badge": "PACOTE COMPLETO • CONDIÇÃO DE LANÇAMENTO",
        "offer_title": "O Que Você Vai Receber Hoje",
        "offer_desc": "Acesso imediato no seu e-mail após confirmação do pagamento.",
        "offer_card_tag": "🔥 OFERTA EXCLUSIVA NA ESCALE PAY",
        "item1_title": "E-book Mente Inabalável",
        "item1_desc": "O Código do Homem Frio, Focado e Implacável (PDF Completo - Entrega Imediata)",
        "item2_badge": "BÔNUS 1",
        "item2_title": "Protocolo de 21 Dias",
        "item2_desc": "Uma ação diária prática para reconfigurar seus hábitos e parar de falhar.",
        "item3_badge": "BÔNUS 2",
        "item3_title": "Checklist Diário do Implacável",
        "item3_desc": "Folha prática de rotina matinal, diurna e noturna para imprimir e colar na parede.",
        "free_tag": "GRÁTIS",
        "included_tag": "Incluso",
        "total_val_label": "Valor Total Acumulado:",
        "promo_price_label": "Preço Promocional de Lançamento:",
        "payment_type_label": "Pagamento Único • Sem Mensalidades",
        "cta_offer": "ATIVAR MEU CÓDIGO AGORA (147MT)",
        "secure_proc": "Pagamento 100% seguro processado via <strong>Escale Pay</strong>",
        "compat_title": "Aviso de Compatibilidade",
        "compat_desc": "Este material não é para todo mundo. Seja sincero com o que você procura:",
        "not_for_title": "NÃO É PARA QUEM:",
        "not_for_1": "Procura 'fórmula mágica' ou quer mudar sem fazer esforço real.",
        "not_for_2": "Ama se fazer de vítima e culpar o governo, a família ou o destino.",
        "not_for_3": "Quer ler 'textinho bonito de autoajuda' para se emocionar por 5 minutos e continuar na mesma.",
        "for_title": "É EXATAMENTE PARA QUEM:",
        "for_1": "Está cansado de ser refém da própria preguiça, do celular e da distração.",
        "for_2": "Quer construir respeito próprio, foco blindado e disciplina silenciosa.",
        "for_3": "Está disposto a executar 1 ação por dia sem negociar consigo mesmo.",
        "guar_badge": "RISCO ZERO • GARANTIA TOTAL",
        "guar_title": "7 Dias de Garantia Incondicional",
        "guar_desc": "Você entra, lê o livro completo e aplica o Protocolo de 21 Dias. Se em 7 dias você achar que o conteúdo não te tornou um homem mais focado e frio, basta solicitar o reembolso na plataforma.",
        "guar_bold": "Devolvemos 100% do seu dinheiro. Sem perguntas e sem letras miúdas.",
        "final_title": "Ninguém vem te salvar.",
        "final_title_gold": "A decisão é sua.",
        "final_desc": "Enquanto você adia, a sua vida passa. Você pode continuar no mesmo ciclo de desculpas, ou pagar <strong style='color:#F59E0B'>147MT</strong> agora e ativar o código que vai blindar a sua mente.",
        "final_cta": "QUERO MINHA MENTE INABALÁVEL AGORA",
        "final_urgency": "⚡ Condição de lançamento válida apenas enquanto restarem vagas via Escale Pay",
        "faq_badge": "DÚVIDAS FREQUENTES",
        "faq_title": "Perguntas Frequentes",
        "faq1_q": "1. Como vou receber o e-book e os bônus?",
        "faq1_a": "O material é 100% digital em formato PDF de alta qualidade. Assim que o pagamento for aprovado pela plataforma Escale Pay, o link de download e acesso imediato é enviado direto para o seu e-mail.",
        "faq2_q": "2. Quais são as formas de pagamento?",
        "faq2_a": "Você pode pagar com total segurança em Moçambique via M-Pesa, E-Mola ou cartão de débito/crédito na plataforma Escale Pay pelo valor promocional de 147 MT.",
        "faq3_q": "3. Serve para quem nunca leu nada sobre estoicismo?",
        "faq3_a": "Sim! O livro foi escrito em linguagem direta, sem enrolação acadêmica e sem termos difíceis. É 100% focado na execução prática para o seu dia a dia.",
        "faq4_q": "4. Quanto tempo do meu dia eu preciso dedicar?",
        "faq4_a": "Apenas 15 minutos de leitura por dia somados a uma ação prática de 10 minutos recomendada no Protocolo de 21 Dias.",
        "faq5_q": "5. Como funciona a garantia de 7 dias?",
        "faq5_a": "Você tem 7 dias para ler o conteúdo e aplicar o protocolo. Se sentir que não valeu a pena, basta solicitar o estorno na plataforma e você recebe 100% do valor de volta.",
        "sticky_btn": "COMPRAR NA ESCALE PAY (147MT)"
    },
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
        "payment_methods": "⚡ PIX • 💳 Cartão de Crédito • 🅿️ PayPal",
        "badge_top": "CONDIÇÃO EXCLUSIVA DE LANÇAMENTO NO BRASIL",
        "scarcity_text": "Restam apenas 7 vagas com preço promocional",
        "hook_badge": "GUIA OFICIAL DO PERFIL MENTE INABALÁVEL",
        "headline_start": "PARE DE",
        "headline_highlight": "NEGOCIAR COM VOCÊ MESMO",
        "headline_end": "E ASSUMA O CONTROLE.",
        "subheadline": "O sistema estoico e prático para jovens que querem eliminar a procrastinação, dominar as próprias emoções e construir disciplina inabalável em 21 dias.",
        "image_badge": "📦 E-BOOK EM PDF + 2 BÔNUS PRÁTICOS • ENTREGA IMEDIATA",
        "cta_hero": "QUERO ATIVAR MINHA MENTE INABALÁVEL",
        "trust_secure": "Compra 100% Segura via Hotmart",
        "trust_instant": "Entrega Imediata via PIX e Cartão",
        "trust_guarantee": "Garantia de 7 Dias",
        "problem_badge": "A REALIDADE NUA E CRUA",
        "problem_title": "Você já sabe o que fazer.",
        "problem_title_red": "O problema é que você não faz.",
        "problem_p1": "Você não está aqui por falta de informação. Já sabe que precisa acordar no horário. Já sabe que o celular está te comendo vivo. Já sabe exatamente qual vício está te matando devagar.",
        "problem_p2": "À noite, assistindo a um vídeo com trilha épica no TikTok, você promete que <strong style='color:#fff'>'amanhã tudo vai ser diferente'</strong>. Sente aquele arrepio de motivação às 23h.",
        "problem_p3": "Mas às 6h da manhã, o arrepio já morreu. Você aperta a soneca três vezes, acorda arrastado, pega o celular antes de levantar e passa 40 minutos rolando a tela no automático.",
        "problem_quote": "O problema nunca foi falta de vontade. O problema é que você negocia com você mesmo todos os dias. <strong style='color:#F59E0B'>E você sempre perde.</strong>",
        "turn_badge": "A VIRADA DE CHAVE",
        "turn_title": "Motivação é combustível fraco.",
        "turn_title_gold": "O que você precisa é de um motor.",
        "turn_p1": "Te ensinaram que mudança começa com motivação. Isso é uma armadilha. Motivação é emoção. Emoção é clima: muda toda hora. Ninguém constrói um império esperando o dia estar ensolarado.",
        "turn_p2": "O motor não pergunta se você está inspirado. <strong style='color:#fff'>Ele simplesmente liga e executa.</strong>",
        "turn_p3": "O que te falta não é mais um vídeo motivacional. O que te falta é um <strong style='color:#FDE68A'>sistema mental inegociável</strong>: estoicismo aplicado para dominar o que acontece dentro de você, e frieza estratégica para lidar com o que acontece fora.",
        "pillar1_title": "🛡️ ESTOICISMO APLICADO",
        "pillar1_desc": "Para governar impulsos, destruir a ansiedade e controlar a única coisa que realmente depende de você: suas escolhas.",
        "pillar2_title": "⚔️ FRIEZA ESTRATÉGICA",
        "pillar2_desc": "Para agir sem plateia, cortar distrações sem culpa e se tornar ilegível e imune a provocações alheias.",
        "quiz_badge": "⚡ TESTE DO ESPELHO • SEM MEIO-TERMO",
        "quiz_title": "Questionário de Confronto",
        "quiz_desc": "Seja brutalmente sincero consigo mesmo antes de continuar lendo. Marque a sua escolha:",
        "q1_title": "Você quer mudar de verdade ou quer continuar assim?",
        "q1_weak": "Continuar adiando e esperando uma 'motivação mágica' aparecer",
        "q1_strong": "Assumir o controle agora e pagar o preço da disciplina",
        "q2_title": "Depois de mais um dia igual e sem resultado, o que você escolhe?",
        "q2_weak": "Mais um dia de desculpas confortáveis para aliviar a culpa",
        "q2_strong": "Construir hoje o primeiro tijolo de um homem inabalável",
        "q3_title": "Quem decide o seu humor e as suas ações hoje?",
        "q3_weak": "As notificações do celular, o que os outros dizem e o clima",
        "q3_strong": "Eu. Absolutamente nada e ninguém me tira do eixo.",
        "quiz_feedback_title": "Se você marcou a opção do implacável, o próximo passo é este:",
        "quiz_feedback_desc": "A conversa fiada acaba aqui. Chega de viver de promessas não cumpridas. Seu desconto exclusivo de lançamento foi ativado:",
        "quiz_feedback_btn": "DESBLOQUEAR O CÓDIGO (R$ 19,90)",
        "features_badge": "CONTEÚDO PRÁTICO",
        "features_title": "O Que Você Vai Dominar na Prática",
        "features_desc": "Ferramentas brutas para você aplicar imediatamente no seu dia a dia:",
        "f1_title": "A Regra dos 6 Segundos",
        "f1_desc": "Como atravessar o pico emocional sem agir, matar discussões inúteis e nunca mais mandar mensagens que você vai se arrepender.",
        "f2_title": "A Morte das Desculpas",
        "f2_desc": "O corte de linguagem cirúrgico: troque 'não deu tempo' por 'não foi prioridade' e veja sua mente parar de inventar desculpas.",
        "f3_title": "Frieza & Silêncio Estratégico",
        "f3_desc": "Por que quem fala primeiro entrega vantagem. Aprenda a executar seus planos em silêncio absoluto até o resultado aparecer.",
        "f4_title": "O Inventário de Drenos",
        "f4_desc": "Como cortar pessoas tóxicas, telas viciantes e hábitos fracos sem briga, sem drama e aplicando atrito inteligente.",
        "f5_title": "A Dicotomia do Controle",
        "f5_desc": "A regra milenar para parar de sofrer por opinião dos outros, trânsito ou passado, investindo 100% de energia nas suas ações.",
        "f6_title": "Seu Código Pessoal",
        "f6_desc": "Como definir no máximo 7 regras inegociáveis com punições reais para nunca mais tomar decisões fracas no calor do momento.",
        "auth_badge": "AUTORIDADE MILENAR",
        "auth_title": "Não é achismo de internet.",
        "auth_title_gold": "É a doutrina dos imperadores.",
        "auth_desc": "Este método não foi inventado em um vídeo passageiro. É a síntese prática dos princípios que mantiveram homens inabaláveis diante de guerras e crises:",
        "auth1": "<strong style='color:#F59E0B'>🏛️ Marco Aurélio:</strong> O imperador de Roma que governava exércitos e treinava a mente todas as noites para não ser controlado pela vaidade.",
        "auth2": "<strong style='color:#F59E0B'>📜 Sêneca:</strong> O conselheiro imperial que provou que a mente fraca sofre mais na imaginação do que na realidade.",
        "auth3": "<strong style='color:#F59E0B'>⚔️ Epicteto:</strong> O homem que nasceu escravo, conquistou a liberdade interior e ensinou que ninguém tem poder sobre a sua mente a menos que você permita.",
        "auth_footer": "Traduzido de forma cirúrgica para o jovem de hoje: foco, telas, vícios e disciplina de aço.",
        "offer_badge": "PACOTE COMPLETO • CONDIÇÃO DE LANÇAMENTO",
        "offer_title": "O Que Você Vai Receber Hoje",
        "offer_desc": "Acesso imediato no seu e-mail após confirmação do pagamento.",
        "offer_card_tag": "🔥 OFERTA EXCLUSIVA NA HOTMART",
        "item1_title": "E-book Mente Inabalável",
        "item1_desc": "O Código do Homem Frio, Focado e Implacável (PDF Completo - Entrega Imediata)",
        "item2_badge": "BÔNUS 1",
        "item2_title": "Protocolo de 21 Dias",
        "item2_desc": "Uma ação diária prática para reconfigurar seus hábitos e parar de falhar.",
        "item3_badge": "BÔNUS 2",
        "item3_title": "Checklist Diário do Implacável",
        "item3_desc": "Folha prática de rotina matinal, diurna e noturna para imprimir e colar na parede.",
        "free_tag": "GRÁTIS",
        "included_tag": "Incluso",
        "total_val_label": "Valor Total Acumulado:",
        "promo_price_label": "Preço Promocional de Lançamento:",
        "payment_type_label": "Pagamento Único via PIX ou Cartão",
        "cta_offer": "ATIVAR MEU CÓDIGO AGORA (R$ 19,90)",
        "secure_proc": "Pagamento 100% seguro processado via <strong>Hotmart</strong>",
        "compat_title": "Aviso de Compatibilidade",
        "compat_desc": "Este material não é para todo mundo. Seja sincero com o que você procura:",
        "not_for_title": "NÃO É PARA QUEM:",
        "not_for_1": "Procura 'fórmula mágica' ou quer mudar sem fazer esforço real.",
        "not_for_2": "Ama se fazer de vítima e culpar o governo, a família ou o destino.",
        "not_for_3": "Quer ler 'textinho bonito de autoajuda' para se emocionar por 5 minutos e continuar na mesma.",
        "for_title": "É EXATAMENTE PARA QUEM:",
        "for_1": "Está cansado de ser refém da própria preguiça, do celular e da distração.",
        "for_2": "Quer construir respeito próprio, foco blindado e disciplina silenciosa.",
        "for_3": "Está disposto a executar 1 ação por dia sem negociar consigo mesmo.",
        "guar_badge": "RISCO ZERO • GARANTIA TOTAL",
        "guar_title": "7 Dias de Garantia Incondicional",
        "guar_desc": "Você entra, lê o livro completo e aplica o Protocolo de 21 Dias. Se em 7 dias você achar que o conteúdo não te tornou um homem mais focado e frio, basta solicitar o reembolso na Hotmart.",
        "guar_bold": "Devolvemos 100% do seu dinheiro. Sem perguntas e sem letras miúdas.",
        "final_title": "Ninguém vem te salvar.",
        "final_title_gold": "A decisão é sua.",
        "final_desc": "Enquanto você adia, a sua vida passa. Você pode continuar no mesmo ciclo de desculpas, ou pagar <strong style='color:#F59E0B'>R$ 19,90</strong> agora e ativar o código que vai blindar a sua mente.",
        "final_cta": "QUERO MINHA MENTE INABALÁVEL AGORA",
        "final_urgency": "⚡ Condição de lançamento válida apenas para as vagas de hoje via Hotmart",
        "faq_badge": "DÚVIDAS FREQUENTES",
        "faq_title": "Perguntas Frequentes",
        "faq1_q": "1. Como vou receber o e-book e os bônus?",
        "faq1_a": "O material é 100% digital em formato PDF de alta qualidade. Assim que o pagamento for aprovado pela Hotmart, o link de download e acesso imediato é enviado direto para o seu e-mail.",
        "faq2_q": "2. Quais são as formas de pagamento?",
        "faq2_a": "Você pode pagar via PIX com liberação instantânea, Cartão de Crédito ou PayPal diretamente pela plataforma segura da Hotmart por apenas R$ 19,90.",
        "faq3_q": "3. Serve para quem nunca leu nada sobre estoicismo?",
        "faq3_a": "Sim! O livro foi escrito em linguagem direta, sem enrolação acadêmica e sem termos difíceis. É 100% focado na execução prática para o seu dia a dia.",
        "faq4_q": "4. Quanto tempo do meu dia eu preciso dedicar?",
        "faq4_a": "Apenas 15 minutos de leitura por dia somados a uma ação prática de 10 minutos recomendada no Protocolo de 21 Dias.",
        "faq5_q": "5. Como funciona a garantia de 7 dias?",
        "faq5_a": "Você tem 7 dias para ler o conteúdo e aplicar o protocolo. Se sentir que não valeu a pena, basta solicitar o estorno na Hotmart e você recebe 100% do valor de volta.",
        "sticky_btn": "COMPRAR NO BRASIL (R$ 19,90)"
    },
    "US": {
        "lang_code": "en-US",
        "country_name": "United States",
        "flag": "🇺🇸",
        "currency_symbol": "$",
        "price_anchor": "$29.99",
        "price_total": "$39.99",
        "price_current": "$4.99",
        "price_ebook": "$19.99",
        "price_b1": "$10.00",
        "price_b2": "$10.00",
        "checkout_url": "https://pay.hotmart.com/B107479792A",
        "checkout_platform": "Hotmart",
        "payment_methods": "💳 Credit/Debit Card • 🅿️ PayPal • 📱 Apple Pay / Google Pay",
        "badge_top": "LIMITED LAUNCH OFFER • WORLDWIDE ACCESS",
        "scarcity_text": "Only 7 discounted spots remaining today",
        "hook_badge": "OFFICIAL UNBREAKABLE MIND GUIDE",
        "headline_start": "STOP",
        "headline_highlight": "NEGOTIATING WITH YOURSELF",
        "headline_end": "AND TAKE CONTROL.",
        "subheadline": "The practical stoic system for young men who want to crush procrastination, master their emotions, and build unbreakable discipline in 21 days.",
        "image_badge": "📦 FULL PDF E-BOOK + 2 ACTIONABLE BONUSES • INSTANT DELIVERY",
        "cta_hero": "ACTIVATE MY UNBREAKABLE MIND",
        "trust_secure": "100% Secure Checkout via Hotmart",
        "trust_instant": "Instant Access to Your Email",
        "trust_guarantee": "7-Day Money-Back Guarantee",
        "problem_badge": "THE RAW UNFILTERED TRUTH",
        "problem_title": "You already know what to do.",
        "problem_title_red": "The problem is that you never do it.",
        "problem_p1": "You are not here because of a lack of information. You already know you need to wake up on time. You know your phone is consuming your dopamine alive. You know exactly which habit is holding you back.",
        "problem_p2": "At night, watching an epic TikTok video with motivational music, you swear that <strong style='color:#fff'>'tomorrow everything changes'</strong>. You feel that rush of motivation at 11 PM.",
        "problem_p3": "But at 6 AM, that motivation is dead. You hit the snooze button three times, drag yourself out of bed, grab your phone, and spend 40 minutes scrolling on autopilot.",
        "problem_quote": "The problem was never lack of willpower. The problem is that you negotiate with yourself every single day. <strong style='color:#F59E0B'>And you always lose.</strong>",
        "turn_badge": "THE PIVOT",
        "turn_title": "Motivation is cheap fuel.",
        "turn_title_gold": "What you need is an engine.",
        "turn_p1": "They taught you that change starts with motivation. That's a trap. Motivation is an emotion. Emotions change like the weather. Nobody builds an empire waiting for sunny days.",
        "turn_p2": "An engine doesn't ask if you feel inspired. <strong style='color:#fff'>It turns on and performs.</strong>",
        "turn_p3": "You don't need another motivational clip. What you need is a <strong style='color:#FDE68A'>non-negotiable mental system</strong>: applied stoicism to master what happens inside you, and strategic coldness to dominate what happens outside.",
        "pillar1_title": "🛡️ APPLIED STOICISM",
        "pillar1_desc": "To govern impulses, eliminate anxiety, and focus exclusively on what you control: your choices.",
        "pillar2_title": "⚔️ STRATEGIC COLDNESS",
        "pillar2_desc": "To execute in total silence, eliminate distractions without guilt, and become unreadable and immune to external noise.",
        "quiz_badge": "⚡ THE MIRROR TEST • NO EXCUSES",
        "quiz_title": "Confrontation Questionnaire",
        "quiz_desc": "Be brutally honest with yourself before reading further. Make your choice:",
        "q1_title": "Do you truly want to change or keep making excuses?",
        "q1_weak": "Keep delaying and waiting for 'magical motivation' to appear",
        "q1_strong": "Take full control right now and pay the price of discipline",
        "q2_title": "After another wasted day with zero results, what do you choose?",
        "q2_weak": "Another comfortable excuse to soothe my guilt",
        "q2_strong": "Build the first brick of an unbreakable, relentless character",
        "q3_title": "Who dictates your mood and actions today?",
        "q3_weak": "Social notifications, what others say, and random circumstances",
        "q3_strong": "Me. Absolutely nothing and no one throws me off balance.",
        "quiz_feedback_title": "If you chose the relentless option, talk is over.",
        "quiz_feedback_desc": "No more unfulfilled promises. Your exclusive launch discount has been unlocked:",
        "quiz_feedback_btn": "UNLOCK THE CODE ($4.99)",
        "features_badge": "PRACTICAL BLUEPRINT",
        "features_title": "What You Will Master in Practice",
        "features_desc": "Raw, battle-tested tools to apply immediately to your daily life:",
        "f1_title": "The 6-Second Rule",
        "f1_desc": "How to ride out emotional peaks without reacting, destroy pointless arguments, and never say something you'll regret.",
        "f2_title": "The Death of Excuses",
        "f2_desc": "Surgical language reframing: swap 'I didn't have time' for 'It wasn't a priority' and make your word sacred again.",
        "f3_title": "Strategic Coldness & Silence",
        "f3_desc": "Why speaking first gives away leverage. Learn to execute your plans in total silence until the results speak.",
        "f4_title": "The Drain Inventory",
        "f4_desc": "How to cut toxic friendships, addictive screens, and weak habits with zero drama and zero guilt.",
        "f5_title": "The Dichotomy of Control",
        "f5_desc": "The timeless principle to stop suffering over opinions, traffic, or the past, channeling 100% of your energy into action.",
        "f6_title": "Your Personal Code",
        "f6_desc": "How to construct up to 7 non-negotiable rules with real penalties to prevent weak impulses from taking over.",
        "auth_badge": "ANCIENT AUTHORITY",
        "auth_title": "Not internet fluff.",
        "auth_title_gold": "The doctrine of emperors.",
        "auth_desc": "This system wasn't made up for a quick video. It is the practical distillation of the principles that kept men unshakeable during wars and crises:",
        "auth1": "<strong style='color:#F59E0B'>🏛️ Marcus Aurelius:</strong> The Roman Emperor who commanded armies yet trained his mind every night to remain humble and disciplined.",
        "auth2": "<strong style='color:#F59E0B'>📜 Seneca:</strong> The imperial advisor who proved that weak minds suffer far more in imagination than in reality.",
        "auth3": "<strong style='color:#F59E0B'>⚔️ Epictetus:</strong> Born a slave, he conquered supreme inner freedom and taught that no one controls your mind unless you let them.",
        "auth_footer": "Adapted with surgical precision for the modern man: screen addiction, focus, and iron discipline.",
        "offer_badge": "COMPLETE BUNDLE • LAUNCH CONDITION",
        "offer_title": "What You Will Receive Today",
        "offer_desc": "Instant digital access to your email right after checkout.",
        "offer_card_tag": "🔥 EXCLUSIVE OFFER ON HOTMART",
        "item1_title": "Unbreakable Mind E-Book",
        "item1_desc": "The Code of the Cold, Focused and Relentless Man (Full PDF - Instant Delivery)",
        "item2_badge": "BONUS 1",
        "item2_title": "The 21-Day Protocol",
        "item2_desc": "One practical daily action to reconfigure your habits and destroy procrastination.",
        "item3_badge": "BONUS 2",
        "item3_title": "Daily Relentless Checklist",
        "item3_desc": "Printable morning, daily, and evening routine checklist to hang on your wall.",
        "free_tag": "FREE",
        "included_tag": "Included",
        "total_val_label": "Total Value Combined:",
        "promo_price_label": "Special Launch Price:",
        "payment_type_label": "One-Time Payment • No Subscriptions",
        "cta_offer": "ACTIVATE MY CODE NOW ($4.99)",
        "secure_proc": "100% Secure Checkout via <strong>Hotmart</strong>",
        "compat_title": "Compatibility Notice",
        "compat_desc": "This material is not for everyone. Be honest with what you're looking for:",
        "not_for_title": "THIS IS NOT FOR:",
        "not_for_1": "Those looking for 'magic pills' who want change without daily effort.",
        "not_for_2": "Those who love playing the victim and blaming family, society, or luck.",
        "not_for_3": "Those who just want feel-good self-help quotes to feel motivated for 5 minutes and stay in bed.",
        "for_title": "THIS IS STRICTLY FOR:",
        "for_1": "Those tired of being held hostage by laziness, phone addiction, and distraction.",
        "for_2": "Men who want to build self-respect, bulletproof focus, and silent discipline.",
        "for_3": "Those ready to execute 1 practical action every day without negotiating with themselves.",
        "guar_badge": "ZERO RISK • 100% GUARANTEE",
        "guar_title": "7-Day Unconditional Money-Back Guarantee",
        "guar_desc": "Access the complete book and apply the 21-Day Protocol. If within 7 days you feel this didn't make you sharper, colder, and more disciplined, simply request a refund on Hotmart.",
        "guar_bold": "We return 100% of your money. No questions asked.",
        "final_title": "No one is coming to save you.",
        "final_title_gold": "The decision is yours.",
        "final_desc": "While you hesitate, your life slips away. You can continue making excuses, or invest <strong style='color:#F59E0B'>$4.99</strong> right now and activate the code that will shield your mind.",
        "final_cta": "GET MY UNBREAKABLE MIND NOW",
        "final_urgency": "⚡ Special launch price valid only for the remaining spots today",
        "faq_badge": "FREQUENTLY ASKED QUESTIONS",
        "faq_title": "Frequently Asked Questions",
        "faq1_q": "1. How will I receive the e-book and bonuses?",
        "faq1_a": "Everything is 100% digital in high-resolution PDF format. As soon as your payment is confirmed on Hotmart, the download link is sent straight to your email.",
        "faq2_q": "2. What payment methods are accepted?",
        "faq2_a": "You can securely pay via Credit/Debit Card, PayPal, Apple Pay, or Google Pay directly on Hotmart's global checkout.",
        "faq3_q": "3. Is this suitable for beginners to stoicism?",
        "faq3_a": "Yes! The book is written in punchy, direct language with zero boring academic jargon. It is 100% focused on immediate practical execution.",
        "faq4_q": "4. How much time do I need each day?",
        "faq4_a": "Only 15 minutes of reading per day plus a 10-minute daily actionable task outlined in the 21-Day Protocol.",
        "faq5_q": "5. How does the 7-day guarantee work?",
        "faq5_a": "You have a full 7 days to test everything. If you are not satisfied, request a refund on Hotmart and receive 100% of your money back instantly.",
        "sticky_btn": "GET ACCESS NOW ($4.99)"
    },
    "ES": {
        "lang_code": "es-ES",
        "country_name": "España",
        "flag": "🇪🇸",
        "currency_symbol": "€",
        "price_anchor": "29,99€",
        "price_total": "39,99€",
        "price_current": "4,99€",
        "price_ebook": "19,99€",
        "price_b1": "10,00€",
        "price_b2": "10,00€",
        "checkout_url": "https://pay.hotmart.com/B107479792A",
        "checkout_platform": "Hotmart",
        "payment_methods": "💳 Tarjeta de Crédito/Débito • 🅿️ PayPal • 📱 Apple Pay",
        "badge_top": "OFERTA EXCLUSIVA DE LANZAMIENTO EN ESPAÑA",
        "scarcity_text": "Solo quedan 7 plazas con precio promocional hoy",
        "hook_badge": "GUÍA OFICIAL DEL PERFIL MENTE INQUEBRANTABLE",
        "headline_start": "DEJA DE",
        "headline_highlight": "NEGOCIAR CONTIGO MISMO",
        "headline_end": "Y TOMA EL CONTROL.",
        "subheadline": "El sistema estoico y práctico para jóvenes que quieren eliminar la procrastinación, dominar sus emociones y forjar una disciplina inquebrantable en 21 días.",
        "image_badge": "📦 E-BOOK EN PDF + 2 BONOS PRÁCTICOS • ENTREGA INMEDIATA",
        "cta_hero": "ACTIVAR MI MENTE INQUEBRANTABLE",
        "trust_secure": "Pago 100% Seguro vía Hotmart",
        "trust_instant": "Entrega Inmediata a tu Correo",
        "trust_guarantee": "Garantía de 7 Días",
        "problem_badge": "LA CRUDA REALIDAD",
        "problem_title": "Ya sabes lo que tienes que hacer.",
        "problem_title_red": "El problema es que nunca lo haces.",
        "problem_p1": "No estás aquí por falta de información. Ya sabes que tienes que madrugar. Sabes que el móvil te está devorando la dopamina. Sabes exactamente qué hábito te está destruyendo poco a poco.",
        "problem_p2": "Por la noche, viendo un vídeo épico en TikTok, te prometes que <strong style='color:#fff'>'mañana todo será diferente'</strong>. Sientes ese escalofrío de motivación a las 23:00.",
        "problem_p3": "Pero a las 6:00 de la mañana, la motivación ha muerto. Pospones la alarma tres veces, te levantas arrastrándote, coges el móvil y pasas 40 minutos en el feed en piloto automático.",
        "problem_quote": "El problema nunca fue falta de ganas. El problema es que negocias contigo mismo todos los días. <strong style='color:#F59E0B'>Y siempre pierdes.</strong>",
        "turn_badge": "EL GIRO ESTRATÉGICO",
        "turn_title": "La motivación es combustible barato.",
        "turn_title_gold": "Lo que necesitas es un motor.",
        "turn_p1": "Te enseñaron que el cambio empieza con motivación. Eso es una trampa. La motivación es una emoción. Las emociones cambian como el clima. Nadie construye un imperio esperando a que haga buen tiempo.",
        "turn_p2": "El motor no pregunta si te sientes inspirado. <strong style='color:#fff'>Simplemente arranca y ejecuta.</strong>",
        "turn_p3": "No necesitas otro vídeo motivacional. Lo que te falta es un <strong style='color:#FDE68A'>sistema mental innegociable</strong>: estoicismo aplicado para dominar lo que ocurre dentro de ti, y frialdad estratégica para gobernar lo que ocurre fuera.",
        "pillar1_title": "🛡️ ESTOICISMO APLICADO",
        "pillar1_desc": "Para dominar tus impulsos, destruir la ansiedad y enfocarte únicamente en lo que controlas: tus elecciones.",
        "pillar2_title": "⚔️ FRIALDAD ESTRATÉGICA",
        "pillar2_desc": "Para actuar en silencio, cortar distracciones sin culpa y volverte ilegible e inmune a las provocaciones.",
        "quiz_badge": "⚡ EL TEST DEL ESPEJO • SIN EXCUSAS",
        "quiz_title": "Cuestionario de Confrontación",
        "quiz_desc": "Sé brutalmente sincero contigo mismo antes de seguir leyendo. Elige tu postura:",
        "q1_title": "¿De verdad quieres cambiar o prefieres seguir igual?",
        "q1_weak": "Seguir posponiendo y esperando a que aparezca una 'motivación mágica'",
        "q1_strong": "Tomar el control ahora mismo y pagar el precio de la disciplina",
        "q2_title": "Tras otro día sin resultados, ¿qué eliges?",
        "q2_weak": "Otra excusa cómoda para calmar mi culpa",
        "q2_strong": "Construir hoy el primer ladrillo de un hombre implacable",
        "q3_title": "¿Quién decide tu estado de ánimo y tus acciones hoy?",
        "q3_weak": "Las notificaciones del móvil, lo que dicen los demás y el entorno",
        "q3_strong": "Yo. Absolutamente nada ni nadie me saca de mi eje.",
        "quiz_feedback_title": "Si elegiste la opción del implacable, se acabaron las excusas.",
        "quiz_feedback_desc": "Basta de promesas incumplidas. Tu descuento exclusivo de lanzamiento ha sido desbloqueado:",
        "quiz_feedback_btn": "DESBLOQUEAR EL CÓDIGO (4,99€)",
        "features_badge": "CONTENIDO PRÁCTICO",
        "features_title": "Lo Que Vas a Dominar en la Práctica",
        "features_desc": "Herramientas directas para aplicar inmediatamente en tu día a día:",
        "f1_title": "La Regla de los 6 Segundos",
        "f1_desc": "Cómo atravesar el pico emocional sin reaccionar, fulminar discusiones inútiles y no volver a decir algo de lo que te arrepientas.",
        "f2_title": "La Muerte de las Excusas",
        "f2_desc": "Reencuadre quirúrgico del lenguaje: cambia 'no tuve tiempo' por 'no fue mi prioridad' y haz que tu palabra vuelva a tener valor.",
        "f3_title": "Frialdad y Silencio Estratégico",
        "f3_desc": "Por qué quien habla primero entrega ventaja. Aprende a ejecutar tus metas en silencio absoluto hasta que el resultado hable.",
        "f4_title": "El Inventario de Drenajes",
        "f4_desc": "Cómo cortar amistades tóxicas, pantallas adictivas y hábitos débiles sin drama y sin culpa.",
        "f5_title": "La Dicotomía del Control",
        "f5_desc": "El principio milenario para dejar de sufrir por opiniones ajenas o el pasado, invirtiendo el 100% de tu energía en tus acciones.",
        "f6_title": "Tu Código Personal",
        "f6_desc": "Cómo definir un máximo de 7 reglas innegociables con consecuencias reales para no volver a tomar decisiones débiles en caliente.",
        "auth_badge": "AUTORIDAD MILENARIA",
        "auth_title": "No son modas de internet.",
        "auth_title_gold": "Es la doctrina de los emperadores.",
        "auth_desc": "Este método no se inventó para un vídeo pasajero. Es la síntesis práctica de los principios que mantuvieron firmes a hombres en guerras y crisis:",
        "auth1": "<strong style='color:#F59E0B'>🏛️ Marco Aurelio:</strong> El emperador de Roma que gobernaba ejércitos y entrenaba su mente cada noche para no ser dominado por la vanidad.",
        "auth2": "<strong style='color:#F59E0B'>📜 Séneca:</strong> El sabio imperial que demostró que la mente débil sufre mucho más en la imaginación que en la realidad.",
        "auth3": "<strong style='color:#F59E0B'>⚔️ Epicteto:</strong> Nació esclavo, conquistó la libertad interior suprema y enseñó que nadie controla tu mente a menos que tú se lo permitas.",
        "auth_footer": "Adaptado con precisión quirúrgica para el joven de hoy: foco, dopamina, pantallas y disciplina de hierro.",
        "offer_badge": "PAQUETE COMPLETO • CONDICIÓN DE LANZAMIENTO",
        "offer_title": "Lo Que Recibirás Hoy",
        "offer_desc": "Acceso digital inmediato en tu correo tras confirmar el pago.",
        "offer_card_tag": "🔥 OFERTA EXCLUSIVA EN HOTMART",
        "item1_title": "E-book Mente Inquebrantable",
        "item1_desc": "El Código del Hombre Frío, Enfocado e Implacable (PDF Completo - Entrega Inmediata)",
        "item2_badge": "BONO 1",
        "item2_title": "Protocolo de 21 Días",
        "item2_desc": "Una acción práctica al día para reconfigurar tus hábitos y destruir la procrastinación.",
        "item3_badge": "BONO 2",
        "item3_title": "Checklist Diario del Implacable",
        "item3_desc": "Plantilla de rutina matutina, diurna y nocturna para imprimir y colgar en la pared.",
        "free_tag": "GRATIS",
        "included_tag": "Incluido",
        "total_val_label": "Valor Total Acumulado:",
        "promo_price_label": "Precio Promocional de Lanzamiento:",
        "payment_type_label": "Pago Único • Sin Suscripciones",
        "cta_offer": "ACTIVAR MI CÓDIGO AHORA (4,99€)",
        "secure_proc": "Pago 100% seguro procesado vía <strong>Hotmart</strong>",
        "compat_title": "Aviso de Compatibilidad",
        "compat_desc": "Este material no es para todo el mundo. Sé sincero con lo que buscas:",
        "not_for_title": "NO ES PARA QUIEN:",
        "not_for_1": "Busca 'fórmulas mágicas' o quiere cambiar sin hacer ningún esfuerzo diario.",
        "not_for_2": "Le encanta hacerse la víctima y culpar al gobierno, a la familia o a la suerte.",
        "not_for_3": "Solo quiere leer frases bonitas de autoayuda para sentirse bien 5 minutos y seguir en la cama.",
        "for_title": "ES EXACTAMENTE PARA QUIEN:",
        "for_1": "Está harto de ser rehén de su propia pereza, del móvil y de la distracción.",
        "for_2": "Quiere forjar respeto propio, enfoque blindado y disciplina silenciosa.",
        "for_3": "Está dispuesto a ejecutar 1 acción al día sin negociar consigo mismo.",
        "guar_badge": "CERO RIESGO • GARANTÍA TOTAL",
        "guar_title": "7 Días de Garantía Incondicional",
        "guar_desc": "Entras, lees el libro completo y aplicas el Protocolo de 21 Días. Si en 7 días sientes que no te ha hecho un hombre más enfocado y frío, pides el reembolso en Hotmart.",
        "guar_bold": "Te devolvemos el 100% de tu dinero. Sin preguntas ni letra pequeña.",
        "final_title": "Nadie vendrá a salvarte.",
        "final_title_gold": "La decisión es tuya.",
        "final_desc": "Mientras lo pospones, la vida pasa. Puedes seguir en el mismo ciclo de excusas, o invertir <strong style='color:#F59E0B'>4,99€</strong> ahora y activar el código que blindará tu mente.",
        "final_cta": "QUIERO MI MENTE INQUEBRANTABLE AHORA",
        "final_urgency": "⚡ Condición de lanzamiento válida solo para las plazas disponibles hoy en Hotmart",
        "faq_badge": "PREGUNTAS FRECUENTES",
        "faq_title": "Preguntas Frecuentes",
        "faq1_q": "1. ¿Cómo recibiré el e-book y los bonos?",
        "faq1_a": "El material es 100% digital en formato PDF de alta resolución. En cuanto se confirme el pago en Hotmart, el enlace de descarga inmediata se envía directo a tu correo electrónico.",
        "faq2_q": "2. ¿Cuáles son las formas de pago?",
        "faq2_a": "Puedes pagar de forma 100% segura mediante Tarjeta de Crédito/Débito o PayPal directamente a través de Hotmart por solo 4,99€.",
        "faq3_q": "3. ¿Sirve si nunca he leído nada sobre estoicismo?",
        "faq3_a": "¡Sí! El libro está escrito en un lenguaje directo, sin rodeos académicos ni términos complejos. Está 100% enfocado en la ejecución práctica diaria.",
        "faq4_q": "4. ¿Cuánto tiempo al día necesito dedicar?",
        "faq4_a": "Solo 15 minutos de lectura al día sumados a una acción práctica de 10 minutos recomendada en el Protocolo de 21 Días.",
        "faq5_q": "5. ¿Cómo funciona la garantía de 7 días?",
        "faq5_a": "Tienes 7 días completos para probar el material. Si no quedas satisfecho, solicitas la devolución en Hotmart y recuperas el 100% de tu dinero inmediatamente.",
        "sticky_btn": "COMPRAR EN ESPAÑA (4,99€)"
    }
}

html_code = """<!DOCTYPE html>
<html lang="pt" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0" />
  <title>MENTE INABALÁVEL — O Código do Homem Frio, Focado e Implacável</title>
  <meta name="description" content="O sistema estoico e prático para jovens que querem eliminar a procrastinação, dominar as próprias emoções e construir disciplina inabalável." />

  <!-- Google Fonts: Inter + Cinzel + Syne -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Inter:wght@300;400;500;600;700;800;900&family=Syne:wght@700;800&display=swap" rel="stylesheet" />

  <style>
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    :root {
      --bg-dark: #07080B;
      --bg-card: #111520;
      --bg-card-subtle: rgba(18, 22, 32, 0.75);
      --border-card: rgba(245, 158, 11, 0.2);
      --gold-primary: #F59E0B;
      --gold-light: #FDE68A;
      --gold-dark: #D97706;
      --text-main: #E2E8F0;
      --text-muted: #94A3B8;
      --red-accent: #EF4444;
      --green-accent: #10B981;
    }

    body {
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.5;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }

    .container-custom {
      width: 100%;
      max-width: 680px;
      margin-left: auto;
      margin-right: auto;
      padding-left: 1.25rem;
      padding-right: 1.25rem;
    }

    .container-wide {
      width: 100%;
      max-width: 860px;
      margin-left: auto;
      margin-right: auto;
      padding-left: 1.25rem;
      padding-right: 1.25rem;
    }

    h1, h2, h3, h4, .font-heading {
      font-family: 'Cinzel', 'Syne', 'Inter', serif;
      font-weight: 800;
      letter-spacing: -0.02em;
    }

    .gold-gradient-text {
      background: linear-gradient(135deg, #FDE68A 0%, #F59E0B 50%, #D97706 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: inline-block;
    }

    .btn-gold {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.65rem;
      background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
      color: #07080B;
      font-weight: 900;
      font-size: 1.05rem;
      text-transform: uppercase;
      letter-spacing: 0.03em;
      padding: 1.15rem 1.75rem;
      border-radius: 1rem;
      text-decoration: none;
      cursor: pointer;
      border: none;
      outline: none;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 0 25px rgba(245, 158, 11, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.4);
      position: relative;
      overflow: hidden;
      text-align: center;
      width: 100%;
    }

    .btn-gold:hover {
      transform: translateY(-2px);
      box-shadow: 0 0 35px rgba(245, 158, 11, 0.65);
      background: linear-gradient(135deg, #FBBF24 0%, #F59E0B 100%);
    }

    .btn-hotmart {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.65rem;
      background: linear-gradient(135deg, #FF5722 0%, #E64A19 100%);
      color: #FFFFFF;
      font-weight: 900;
      font-size: 0.95rem;
      text-transform: uppercase;
      letter-spacing: 0.03em;
      padding: 1.05rem 1.5rem;
      border-radius: 1rem;
      text-decoration: none;
      cursor: pointer;
      border: 1px solid rgba(255, 87, 34, 0.5);
      transition: all 0.25s ease;
      box-shadow: 0 4px 20px rgba(230, 74, 25, 0.35);
      text-align: center;
      width: 100%;
    }

    .glass-card {
      background: rgba(17, 21, 32, 0.85);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1px solid rgba(245, 158, 11, 0.18);
      border-radius: 1.25rem;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }

    .glass-card-hover {
      transition: all 0.3s ease;
    }

    .glass-card-hover:hover {
      border-color: rgba(245, 158, 11, 0.45);
      transform: translateY(-3px);
      box-shadow: 0 12px 35px rgba(245, 158, 11, 0.15);
    }

    .badge-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .badge-gold {
      background: rgba(245, 158, 11, 0.12);
      border: 1px solid rgba(245, 158, 11, 0.35);
      color: #FDE68A;
    }

    .badge-red {
      background: rgba(239, 68, 68, 0.12);
      border: 1px solid rgba(239, 68, 68, 0.35);
      color: #FCA5A5;
    }

    .pulse-glow {
      animation: pulse-glow-anim 2s infinite;
    }

    @keyframes pulse-glow-anim {
      0%, 100% {
        box-shadow: 0 0 20px rgba(245, 158, 11, 0.35);
      }
      50% {
        box-shadow: 0 0 45px rgba(245, 158, 11, 0.65);
      }
    }

    /* Country Flag Pill */
    .country-selector-pill {
      display: inline-flex;
      background: #111522;
      border: 1px solid rgba(245, 158, 11, 0.3);
      padding: 0.25rem 0.4rem;
      border-radius: 9999px;
      gap: 0.25rem;
    }

    .country-btn {
      background: transparent;
      border: none;
      color: #94A3B8;
      font-size: 0.75rem;
      font-weight: 800;
      padding: 0.25rem 0.6rem;
      border-radius: 9999px;
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 0.25rem;
    }

    .country-btn.active {
      background: #F59E0B;
      color: #07080B;
      box-shadow: 0 0 10px rgba(245, 158, 11, 0.5);
    }

    /* Quiz Option */
    .quiz-option {
      background: rgba(14, 18, 28, 0.8);
      border: 1px solid #1E2538;
      border-radius: 0.875rem;
      padding: 1rem 1.15rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
      cursor: pointer;
      transition: all 0.2s ease;
      user-select: none;
    }

    .quiz-option:hover {
      background: rgba(24, 30, 48, 0.9);
      border-color: #334155;
    }

    .quiz-option.selected-weak {
      background: rgba(239, 68, 68, 0.12);
      border-color: #EF4444;
      color: #FCA5A5;
    }

    .quiz-option.selected-strong {
      background: rgba(245, 158, 11, 0.15);
      border-color: #F59E0B;
      color: #FDE68A;
      box-shadow: 0 0 15px rgba(245, 158, 11, 0.25);
    }

    .radio-circle {
      width: 1.35rem;
      height: 1.35rem;
      border-radius: 50%;
      border: 2px solid #475569;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      font-weight: 800;
      flex-shrink: 0;
      transition: all 0.2s ease;
    }

    .faq-item {
      background: rgba(17, 21, 32, 0.85);
      border: 1px solid #1E2538;
      border-radius: 1rem;
      overflow: hidden;
      margin-bottom: 0.75rem;
      transition: all 0.25s ease;
    }

    .faq-btn {
      width: 100%;
      padding: 1.15rem 1.25rem;
      background: transparent;
      border: none;
      color: #FFFFFF;
      font-weight: 700;
      font-size: 0.95rem;
      text-align: left;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      cursor: pointer;
    }

    .faq-body {
      padding: 0 1.25rem 1.15rem 1.25rem;
      color: #94A3B8;
      font-size: 0.875rem;
      line-height: 1.6;
      display: none;
      border-top: 1px solid rgba(255, 255, 255, 0.05);
      margin-top: -0.25rem;
      padding-top: 0.75rem;
    }

    .faq-body.open {
      display: block;
    }

    #stickyBar {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(10, 13, 20, 0.96);
      backdrop-filter: blur(12px);
      border-top: 1px solid rgba(245, 158, 11, 0.3);
      padding: 0.75rem 1rem;
      z-index: 90;
      transform: translateY(100%);
      transition: transform 0.3s ease;
    }

    #stickyBar.visible {
      transform: translateY(0);
    }

    @media (min-width: 768px) {
      #stickyBar {
        display: none !important;
      }
    }

    /* Modal Welcome Country Selector */
    #countryModal {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.92);
      backdrop-filter: blur(12px);
      z-index: 9999;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.25rem;
    }

    .modal-country-card {
      background: rgba(14, 18, 28, 0.95);
      border: 1px solid rgba(245, 158, 11, 0.35);
      border-radius: 1.5rem;
      padding: 1.75rem 1.5rem;
      max-width: 460px;
      width: 100%;
      text-align: center;
      box-shadow: 0 20px 50px rgba(0,0,0,0.8);
    }

    .modal-country-option {
      background: #111522;
      border: 1px solid #1E2538;
      border-radius: 1rem;
      padding: 1rem 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      margin-bottom: 0.75rem;
      cursor: pointer;
      transition: all 0.2s ease;
      text-align: left;
    }

    .modal-country-option:hover {
      border-color: #F59E0B;
      background: rgba(245, 158, 11, 0.1);
      transform: translateY(-2px);
    }

    #tiiny-banner, [id*="tiiny"], [class*="tiiny"], a[href*="tiiny.host"] {
      display: none !important;
      visibility: hidden !important;
      opacity: 0 !important;
      height: 0 !important;
      width: 0 !important;
      pointer-events: none !important;
    }

    ::-webkit-scrollbar {
      width: 8px;
    }
    ::-webkit-scrollbar-track {
      background: #07080B;
    }
    ::-webkit-scrollbar-thumb {
      background: #1E2536;
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #F59E0B;
    }
  </style>
</head>

<body>

  <!-- ========================================================================= -->
  <!-- COUNTRY MODAL ON FIRST VISIT (BR / US / ES / MZ) -->
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
        Choose your country / Selecciona tu país para ver en tu moneda:
      </p>

      <div style="display: flex; flex-direction: column;">
        <!-- Option BR -->
        <div onclick="selectCountry('BR')" class="modal-country-option">
          <div style="display: flex; align-items: center; gap: 0.75rem;">
            <span style="font-size: 1.5rem;">🇧🇷</span>
            <div>
              <strong style="color: #FFFFFF; font-size: 0.9rem; display: block;">Brasil (BR)</strong>
              <span style="font-size: 0.7rem; color: #94A3B8;">PIX, Cartão e Boleto • R$ 19,90</span>
            </div>
          </div>
          <span style="color: #F59E0B; font-weight: 800; font-size: 0.9rem;">→</span>
        </div>

        <!-- Option US -->
        <div onclick="selectCountry('US')" class="modal-country-option">
          <div style="display: flex; align-items: center; gap: 0.75rem;">
            <span style="font-size: 1.5rem;">🇺🇸</span>
            <div>
              <strong style="color: #FFFFFF; font-size: 0.9rem; display: block;">United States (US)</strong>
              <span style="font-size: 0.7rem; color: #94A3B8;">English • Card / PayPal • $4.99</span>
            </div>
          </div>
          <span style="color: #F59E0B; font-weight: 800; font-size: 0.9rem;">→</span>
        </div>

        <!-- Option ES -->
        <div onclick="selectCountry('ES')" class="modal-country-option">
          <div style="display: flex; align-items: center; gap: 0.75rem;">
            <span style="font-size: 1.5rem;">🇪🇸</span>
            <div>
              <strong style="color: #FFFFFF; font-size: 0.9rem; display: block;">España (ES)</strong>
              <span style="font-size: 0.7rem; color: #94A3B8;">Español • Tarjeta / PayPal • 4,99€</span>
            </div>
          </div>
          <span style="color: #F59E0B; font-weight: 800; font-size: 0.9rem;">→</span>
        </div>

        <!-- Option MZ -->
        <div onclick="selectCountry('MZ')" class="modal-country-option">
          <div style="display: flex; align-items: center; gap: 0.75rem;">
            <span style="font-size: 1.5rem;">🇲🇿</span>
            <div>
              <strong style="color: #FFFFFF; font-size: 0.9rem; display: block;">Moçambique (MZ)</strong>
              <span style="font-size: 0.7rem; color: #94A3B8;">M-Pesa e E-Mola • 147 MT</span>
            </div>
          </div>
          <span style="color: #F59E0B; font-weight: 800; font-size: 0.9rem;">→</span>
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
        <button id="btn-MZ" onclick="selectCountry('MZ')" class="country-btn active">🇲🇿 MZ</button>
        <button id="btn-BR" onclick="selectCountry('BR')" class="country-btn">🇧🇷 BR</button>
        <button id="btn-US" onclick="selectCountry('US')" class="country-btn">🇺🇸 US</button>
        <button id="btn-ES" onclick="selectCountry('ES')" class="country-btn">🇪🇸 ES</button>
      </div>

      <div style="display: flex; align-items: center; gap: 0.75rem; font-size: 0.75rem; margin: 0 auto;">
        <span style="color: #94A3B8;">Timer:</span>
        <span id="countdown" style="font-family: monospace; font-weight: 900; background: #000; color: #F59E0B; padding: 0.15rem 0.5rem; border-radius: 0.35rem; border: 1px solid rgba(245, 158, 11, 0.4);">
          14:59
        </span>
        <span id="t-scarcity" style="color: #10B981; font-weight: 700;">• 7 vagas restantes</span>
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

      <!-- 1. HEADLINE PRINCIPAL -->
      <h1 style="font-size: clamp(1.85rem, 6.5vw, 2.75rem); line-height: 1.15; text-transform: uppercase; margin-bottom: 1.25rem; color: #FFFFFF;">
        <span id="t-headline-start">PARE DE</span> <span id="t-headline-highlight" class="gold-gradient-text">NEGOCIAR COM VOCÊ MESMO</span> <span id="t-headline-end">E ASSUMA O CONTROLE.</span>
      </h1>

      <!-- 2. SUBHEADLINE -->
      <p id="t-subheadline" style="font-size: clamp(0.95rem, 3.5vw, 1.15rem); color: #CBD5E1; font-weight: 500; line-height: 1.6; margin-bottom: 1.75rem; max-width: 580px; margin-left: auto; margin-right: auto;">
        O sistema estoico e prático para jovens que querem eliminar a procrastinação, dominar as próprias emoções e construir disciplina inabalável em 21 dias.
      </p>

      <!-- 3D EBOOK MOCKUP VISUAL -->
      <div style="position: relative; margin: 1.5rem auto 2rem auto; max-width: 520px;">
        <div style="background: linear-gradient(180deg, rgba(245,158,11,0.25) 0%, rgba(18,22,32,0.6) 100%); padding: 0.5rem; border-radius: 1.5rem; border: 1px solid rgba(245,158,11,0.35); box-shadow: 0 20px 50px rgba(0,0,0,0.8);">
          <img 
            src="IMAGE_EBOOK_PLACEHOLDER" 
            alt="Ebook Mente Inabalável" 
            style="width: 100%; height: auto; border-radius: 1.15rem; display: block;"
          />
        </div>
        <div id="t-image-badge" style="position: absolute; bottom: -0.75rem; left: 50%; transform: translateX(-50%); background: #0B0E17; border: 1px solid rgba(245, 158, 11, 0.5); padding: 0.4rem 1.1rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 800; color: #FDE68A; white-space: nowrap; box-shadow: 0 8px 20px rgba(0,0,0,0.7);">
          📦 E-BOOK EM PDF + 2 BÔNUS PRÁTICOS • ENTREGA IMEDIATA
        </div>
      </div>

      <!-- Price & Hero CTA -->
      <div style="margin-top: 2rem;">
        <div style="display: flex; align-items: baseline; justify-content: center; gap: 0.5rem; margin-bottom: 1rem;">
          <span id="t-price-anchor" style="color: #64748B; font-size: 0.9rem; text-decoration: line-through;">De 597MT</span>
          <span id="t-price-current" style="color: #F59E0B; font-size: 1.85rem; font-weight: 900;">Por apenas 147MT</span>
        </div>

        <a id="t-cta-hero-btn" href="https://checkout.escalepay.com/1889386" target="_blank" class="btn-gold pulse-glow" style="max-width: 480px; margin: 0 auto;">
          <span id="t-cta-hero">QUERO ATIVAR MINHA MENTE INABALÁVEL</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <line x1="5" y1="12" x2="19" y2="12"></line>
            <polyline points="12 5 19 12 12 19"></polyline>
          </svg>
        </a>

        <!-- Micro Trust Signals -->
        <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 1rem; margin-top: 1.25rem; font-size: 0.75rem; color: #94A3B8;">
          <span style="display: flex; align-items: center; gap: 0.35rem;">
            <svg width="14" height="14" viewBox="0 0 20 20" fill="#10B981"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
            <span id="t-trust-secure">Compra 100% Segura</span>
          </span>
          <span style="display: flex; align-items: center; gap: 0.35rem;">
            <svg width="14" height="14" viewBox="0 0 20 20" fill="#10B981"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
            <span id="t-trust-instant">Entrega Imediata</span>
          </span>
          <span style="display: flex; align-items: center; gap: 0.35rem;">
            <svg width="14" height="14" viewBox="0 0 20 20" fill="#10B981"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
            <span id="t-trust-guarantee">Garantia de 7 Dias</span>
          </span>
        </div>
      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 3. ABERTURA / QUEBRA DE PADRÃO -->
  <!-- ========================================================================= -->
  <section style="background: #0B0E15; border-top: 1px solid #1E2538; border-bottom: 1px solid #1E2538; padding: 3rem 0;">
    <div class="container-custom">
      
      <div id="t-problem-badge" class="badge-pill badge-red" style="margin-bottom: 1rem;">
        A REALIDADE NUA E CRUA
      </div>

      <h2 style="font-size: clamp(1.4rem, 5vw, 1.85rem); text-transform: uppercase; color: #FFFFFF; line-height: 1.25; margin-bottom: 1.25rem;">
        <span id="t-problem-title">Você já sabe o que fazer.</span> <br />
        <span id="t-problem-title-red" style="color: #EF4444;">O problema é que você não faz.</span>
      </h2>

      <div style="font-size: 0.95rem; line-height: 1.7; color: #CBD5E1;">
        <p id="t-problem-p1" style="margin-bottom: 1rem;"></p>
        <p id="t-problem-p2" style="margin-bottom: 1rem;"></p>
        <p id="t-problem-p3" style="margin-bottom: 1rem;"></p>
        <div id="t-problem-quote" style="background: #111522; border-left: 4px solid #F59E0B; padding: 1.1rem; border-radius: 0.75rem; margin-top: 1.25rem; color: #E2E8F0;"></div>
      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 4. A VIRADA -->
  <!-- ========================================================================= -->
  <section style="padding: 3.5rem 0; position: relative;">
    <div class="container-custom">
      
      <div id="t-turn-badge" class="badge-pill badge-gold" style="margin-bottom: 1rem;">
        A VIRADA DE CHAVE
      </div>

      <h2 style="font-size: clamp(1.45rem, 5vw, 2rem); text-transform: uppercase; color: #FFFFFF; line-height: 1.2; margin-bottom: 1.25rem;">
        <span id="t-turn-title">Motivação é combustível fraco.</span> <br />
        <span id="t-turn-title-gold" class="gold-gradient-text">O que você precisa é de um motor.</span>
      </h2>

      <div style="font-size: 0.95rem; line-height: 1.7; color: #CBD5E1;">
        <p id="t-turn-p1" style="margin-bottom: 1rem;"></p>
        <p id="t-turn-p2" style="margin-bottom: 1rem;"></p>
        <p id="t-turn-p3" style="margin-bottom: 1.5rem;"></p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem;">
          <div class="glass-card" style="padding: 1.25rem;">
            <div id="t-pillar1-title" style="color: #F59E0B; font-weight: 800; font-size: 0.85rem; margin-bottom: 0.35rem;">🛡️ ESTOICISMO APLICADO</div>
            <p id="t-pillar1-desc" style="font-size: 0.8rem; color: #94A3B8; line-height: 1.5;"></p>
          </div>
          <div class="glass-card" style="padding: 1.25rem;">
            <div id="t-pillar2-title" style="color: #F59E0B; font-weight: 800; font-size: 0.85rem; margin-bottom: 0.35rem;">⚔️ FRIEZA ESTRATÉGICA</div>
            <p id="t-pillar2-desc" style="font-size: 0.8rem; color: #94A3B8; line-height: 1.5;"></p>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 5. QUESTIONÁRIO DE CONFRONTO -->
  <!-- ========================================================================= -->
  <section id="confronto" style="background: #090C14; border-top: 1px solid rgba(245, 158, 11, 0.2); border-bottom: 1px solid rgba(245, 158, 11, 0.2); padding: 3.5rem 0;">
    <div class="container-custom">
      
      <div style="text-align: center; margin-bottom: 2rem;">
        <div id="t-quiz-badge" class="badge-pill badge-gold" style="margin-bottom: 0.75rem;">
          ⚡ TESTE DO ESPELHO • SEM MEIO-TERMO
        </div>
        <h2 id="t-quiz-title" style="font-size: clamp(1.45rem, 5vw, 1.95rem); text-transform: uppercase; color: #FFFFFF; margin-bottom: 0.5rem;">
          Questionário de Confronto
        </h2>
        <p id="t-quiz-desc" style="font-size: 0.85rem; color: #94A3B8; max-width: 480px; margin: 0 auto;">
          Seja brutalmente sincero consigo mesmo antes de continuar lendo. Marque a sua escolha:
        </p>
      </div>

      <div style="display: flex; flex-direction: column; gap: 1.25rem;">
        
        <!-- Q1 -->
        <div class="glass-card" style="padding: 1.25rem;">
          <h3 style="font-size: 0.95rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.85rem; display: flex; gap: 0.5rem;">
            <span style="color: #F59E0B;">01.</span>
            <span id="t-q1-title">Você quer mudar de verdade ou quer continuar assim?</span>
          </h3>
          <div style="display: flex; flex-direction: column; gap: 0.6rem;">
            <div onclick="selectQuiz(1, 'weak', this)" class="quiz-option">
              <span id="t-q1-weak" style="font-size: 0.82rem;"></span>
              <span class="radio-circle"></span>
            </div>
            <div onclick="selectQuiz(1, 'strong', this)" class="quiz-option">
              <span id="t-q1-strong" style="font-size: 0.82rem; font-weight: 700; color: #FFFFFF;"></span>
              <span class="radio-circle"></span>
            </div>
          </div>
        </div>

        <!-- Q2 -->
        <div class="glass-card" style="padding: 1.25rem;">
          <h3 style="font-size: 0.95rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.85rem; display: flex; gap: 0.5rem;">
            <span style="color: #F59E0B;">02.</span>
            <span id="t-q2-title">Depois de mais um dia igual e sem resultado, o que você escolhe?</span>
          </h3>
          <div style="display: flex; flex-direction: column; gap: 0.6rem;">
            <div onclick="selectQuiz(2, 'weak', this)" class="quiz-option">
              <span id="t-q2-weak" style="font-size: 0.82rem;"></span>
              <span class="radio-circle"></span>
            </div>
            <div onclick="selectQuiz(2, 'strong', this)" class="quiz-option">
              <span id="t-q2-strong" style="font-size: 0.82rem; font-weight: 700; color: #FFFFFF;"></span>
              <span class="radio-circle"></span>
            </div>
          </div>
        </div>

        <!-- Q3 -->
        <div class="glass-card" style="padding: 1.25rem;">
          <h3 style="font-size: 0.95rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.85rem; display: flex; gap: 0.5rem;">
            <span style="color: #F59E0B;">03.</span>
            <span id="t-q3-title">Quem decide o seu humor e as suas ações hoje?</span>
          </h3>
          <div style="display: flex; flex-direction: column; gap: 0.6rem;">
            <div onclick="selectQuiz(3, 'weak', this)" class="quiz-option">
              <span id="t-q3-weak" style="font-size: 0.82rem;"></span>
              <span class="radio-circle"></span>
            </div>
            <div onclick="selectQuiz(3, 'strong', this)" class="quiz-option">
              <span id="t-q3-strong" style="font-size: 0.82rem; font-weight: 700; color: #FFFFFF;"></span>
              <span class="radio-circle"></span>
            </div>
          </div>
        </div>

      </div>

      <!-- Quiz Feedback -->
      <div id="quizFeedback" class="glass-card" style="margin-top: 1.75rem; padding: 1.5rem; text-align: center; border: 1px solid #F59E0B; background: linear-gradient(180deg, rgba(245,158,11,0.15) 0%, rgba(17,21,32,0.95) 100%);">
        <div style="width: 44px; height: 44px; margin: 0 auto 0.75rem auto; background: rgba(245,158,11,0.2); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.25rem; color: #F59E0B; border: 1px solid rgba(245,158,11,0.4);">
          ✓
        </div>
        <h4 id="t-quiz-feedback-title" style="font-size: 1.1rem; color: #FFFFFF; text-transform: uppercase; margin-bottom: 0.5rem;"></h4>
        <p id="t-quiz-feedback-desc" style="font-size: 0.82rem; color: #CBD5E1; max-width: 440px; margin: 0 auto 1.25rem auto; line-height: 1.5;"></p>
        <a id="t-quiz-feedback-btn-link" href="#oferta" class="btn-gold" style="max-width: 380px; margin: 0 auto; font-size: 0.95rem; padding: 0.9rem 1.5rem;">
          <span id="t-quiz-feedback-btn">DESBLOQUEAR O CÓDIGO</span>
        </a>
      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 6. O QUE VOCÊ VAI DOMINAR -->
  <!-- ========================================================================= -->
  <section style="padding: 3.5rem 0;">
    <div class="container-wide">
      
      <div style="text-align: center; margin-bottom: 2rem;">
        <div id="t-features-badge" class="badge-pill badge-gold" style="margin-bottom: 0.5rem;">
          CONTEÚDO PRÁTICO
        </div>
        <h2 id="t-features-title" style="font-size: clamp(1.45rem, 5vw, 2rem); text-transform: uppercase; color: #FFFFFF;">
          O Que Você Vai Dominar na Prática
        </h2>
        <p id="t-features-desc" style="font-size: 0.85rem; color: #94A3B8; margin-top: 0.35rem;"></p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem;">
        
        <div class="glass-card glass-card-hover" style="padding: 1.25rem; display: flex; gap: 1rem; align-items: flex-start;">
          <div style="width: 36px; height: 36px; border-radius: 0.65rem; background: rgba(245,158,11,0.15); border: 1px solid rgba(245,158,11,0.3); display: flex; align-items: center; justify-content: center; font-size: 1rem; flex-shrink: 0;">⏱️</div>
          <div>
            <h3 id="t-f1-title" style="font-size: 0.92rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.25rem;"></h3>
            <p id="t-f1-desc" style="font-size: 0.78rem; color: #94A3B8; line-height: 1.5;"></p>
          </div>
        </div>

        <div class="glass-card glass-card-hover" style="padding: 1.25rem; display: flex; gap: 1rem; align-items: flex-start;">
          <div style="width: 36px; height: 36px; border-radius: 0.65rem; background: rgba(245,158,11,0.15); border: 1px solid rgba(245,158,11,0.3); display: flex; align-items: center; justify-content: center; font-size: 1rem; flex-shrink: 0;">🚫</div>
          <div>
            <h3 id="t-f2-title" style="font-size: 0.92rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.25rem;"></h3>
            <p id="t-f2-desc" style="font-size: 0.78rem; color: #94A3B8; line-height: 1.5;"></p>
          </div>
        </div>

        <div class="glass-card glass-card-hover" style="padding: 1.25rem; display: flex; gap: 1rem; align-items: flex-start;">
          <div style="width: 36px; height: 36px; border-radius: 0.65rem; background: rgba(245,158,11,0.15); border: 1px solid rgba(245,158,11,0.3); display: flex; align-items: center; justify-content: center; font-size: 1rem; flex-shrink: 0;">🤐</div>
          <div>
            <h3 id="t-f3-title" style="font-size: 0.92rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.25rem;"></h3>
            <p id="t-f3-desc" style="font-size: 0.78rem; color: #94A3B8; line-height: 1.5;"></p>
          </div>
        </div>

        <div class="glass-card glass-card-hover" style="padding: 1.25rem; display: flex; gap: 1rem; align-items: flex-start;">
          <div style="width: 36px; height: 36px; border-radius: 0.65rem; background: rgba(245,158,11,0.15); border: 1px solid rgba(245,158,11,0.3); display: flex; align-items: center; justify-content: center; font-size: 1rem; flex-shrink: 0;">✂️</div>
          <div>
            <h3 id="t-f4-title" style="font-size: 0.92rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.25rem;"></h3>
            <p id="t-f4-desc" style="font-size: 0.78rem; color: #94A3B8; line-height: 1.5;"></p>
          </div>
        </div>

        <div class="glass-card glass-card-hover" style="padding: 1.25rem; display: flex; gap: 1rem; align-items: flex-start;">
          <div style="width: 36px; height: 36px; border-radius: 0.65rem; background: rgba(245,158,11,0.15); border: 1px solid rgba(245,158,11,0.3); display: flex; align-items: center; justify-content: center; font-size: 1rem; flex-shrink: 0;">🎯</div>
          <div>
            <h3 id="t-f5-title" style="font-size: 0.92rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.25rem;"></h3>
            <p id="t-f5-desc" style="font-size: 0.78rem; color: #94A3B8; line-height: 1.5;"></p>
          </div>
        </div>

        <div class="glass-card glass-card-hover" style="padding: 1.25rem; display: flex; gap: 1rem; align-items: flex-start;">
          <div style="width: 36px; height: 36px; border-radius: 0.65rem; background: rgba(245,158,11,0.15); border: 1px solid rgba(245,158,11,0.3); display: flex; align-items: center; justify-content: center; font-size: 1rem; flex-shrink: 0;">📜</div>
          <div>
            <h3 id="t-f6-title" style="font-size: 0.92rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.25rem;"></h3>
            <p id="t-f6-desc" style="font-size: 0.78rem; color: #94A3B8; line-height: 1.5;"></p>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 7. PROVA / AUTORIDADE FILOSÓFICA -->
  <!-- ========================================================================= -->
  <section style="background: #0A0D15; border-top: 1px solid #1E2538; border-bottom: 1px solid #1E2538; padding: 3.5rem 0;">
    <div class="container-wide">
      
      <div style="display: flex; flex-direction: column; align-items: center; gap: 2rem;">
        
        <div style="width: 100%; max-width: 380px;">
          <div style="background: linear-gradient(135deg, rgba(245,158,11,0.3) 0%, rgba(18,22,32,0.8) 100%); padding: 0.4rem; border-radius: 1.25rem; border: 1px solid rgba(245,158,11,0.3); box-shadow: 0 15px 35px rgba(0,0,0,0.6);">
            <img 
              src="IMAGE_HERO_PLACEHOLDER" 
              alt="Marco Aurélio - Estoicismo Clássico" 
              style="width: 100%; height: auto; border-radius: 1rem; display: block;"
            />
          </div>
        </div>

        <div style="max-width: 600px;">
          <div id="t-auth-badge" class="badge-pill badge-gold" style="margin-bottom: 0.75rem;">
            AUTORIDADE MILENAR
          </div>
          <h2 style="font-size: clamp(1.4rem, 5vw, 1.85rem); text-transform: uppercase; color: #FFFFFF; margin-bottom: 0.75rem; line-height: 1.25;">
            <span id="t-auth-title">Não é achismo de internet.</span> <br />
            <span id="t-auth-title-gold" class="gold-gradient-text">É a doutrina dos imperadores.</span>
          </h2>
          <p id="t-auth-desc" style="font-size: 0.88rem; color: #CBD5E1; line-height: 1.6; margin-bottom: 1rem;"></p>

          <div style="display: flex; flex-direction: column; gap: 0.75rem;">
            <div id="t-auth1" style="background: #111522; padding: 0.85rem 1rem; border-radius: 0.75rem; border: 1px solid #1E2538; font-size: 0.82rem; color: #CBD5E1;"></div>
            <div id="t-auth2" style="background: #111522; padding: 0.85rem 1rem; border-radius: 0.75rem; border: 1px solid #1E2538; font-size: 0.82rem; color: #CBD5E1;"></div>
            <div id="t-auth3" style="background: #111522; padding: 0.85rem 1rem; border-radius: 0.75rem; border: 1px solid #1E2538; font-size: 0.82rem; color: #CBD5E1;"></div>
          </div>

          <p id="t-auth-footer" style="font-size: 0.8rem; color: #FDE68A; margin-top: 1rem; font-weight: 600;"></p>
        </div>

      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 8. O QUE ESTÁ INCLUSO (Oferta Empilhada) -->
  <!-- ========================================================================= -->
  <section id="oferta" style="padding: 3.5rem 0; position: relative;">
    <div class="container-custom">
      
      <div style="text-align: center; margin-bottom: 1.75rem;">
        <div id="t-offer-badge" class="badge-pill badge-gold" style="margin-bottom: 0.5rem;">
          PACOTE COMPLETO • CONDIÇÃO DE LANÇAMENTO
        </div>
        <h2 id="t-offer-title" style="font-size: clamp(1.5rem, 5.5vw, 2.15rem); text-transform: uppercase; color: #FFFFFF;">
          O Que Você Vai Receber Hoje
        </h2>
        <p id="t-offer-desc" style="font-size: 0.85rem; color: #94A3B8; margin-top: 0.25rem;">
          Acesso imediato no seu e-mail após confirmação.
        </p>
      </div>

      <!-- Bundle Mockup Visual -->
      <div style="margin-bottom: 1.75rem; max-width: 480px; margin-left: auto; margin-right: auto;">
        <div style="background: #111522; padding: 0.4rem; border-radius: 1.25rem; border: 1px solid rgba(245,158,11,0.3); box-shadow: 0 15px 40px rgba(0,0,0,0.7);">
          <img 
            src="IMAGE_BUNDLE_PLACEHOLDER" 
            alt="Combo Completo Mente Inabalável" 
            style="width: 100%; height: auto; border-radius: 1rem; display: block;"
          />
        </div>
      </div>

      <!-- THE STACK CARD -->
      <div class="glass-card" style="padding: 1.5rem; border: 2px solid rgba(245,158,11,0.45); box-shadow: 0 0 35px rgba(245,158,11,0.25); position: relative;">
        
        <div id="t-offer-card-tag" style="position: absolute; top: -0.75rem; left: 50%; transform: translateX(-50%); background: linear-gradient(135deg, #F59E0B, #D97706); color: #07080B; font-weight: 900; font-size: 0.72rem; padding: 0.35rem 1rem; border-radius: 9999px; text-transform: uppercase; letter-spacing: 0.05em; white-space: nowrap;">
          🔥 OFERTA EXCLUSIVA DE LANÇAMENTO
        </div>

        <!-- Item 1 -->
        <div style="padding: 1rem 0; border-bottom: 1px solid #1E2538; display: flex; justify-content: space-between; align-items: flex-start; gap: 0.75rem;">
          <div style="display: flex; gap: 0.75rem; align-items: flex-start;">
            <span style="font-size: 1.25rem;">📘</span>
            <div>
              <h3 id="t-item1-title" style="font-size: 0.95rem; font-weight: 800; color: #FFFFFF;"></h3>
              <p id="t-item1-desc" style="font-size: 0.75rem; color: #94A3B8; margin-top: 0.15rem;"></p>
            </div>
          </div>
          <div style="text-align: right; flex-shrink: 0;">
            <span id="t-price-ebook" style="font-size: 0.75rem; color: #64748B; text-decoration: line-through; display: block;"></span>
            <span id="t-included-tag" style="font-size: 0.75rem; font-weight: 800; color: #F59E0B;">Incluso</span>
          </div>
        </div>

        <!-- Item 2 -->
        <div style="padding: 1rem 0; border-bottom: 1px solid #1E2538; display: flex; justify-content: space-between; align-items: flex-start; gap: 0.75rem;">
          <div style="display: flex; gap: 0.75rem; align-items: flex-start;">
            <span style="font-size: 1.25rem;">🎁</span>
            <div>
              <div style="display: flex; align-items: center; gap: 0.35rem;">
                <span id="t-item2-badge" style="background: rgba(245,158,11,0.2); color: #FDE68A; font-size: 0.65rem; font-weight: 800; padding: 0.15rem 0.4rem; border-radius: 0.25rem;">BÔNUS 1</span>
                <h3 id="t-item2-title" style="font-size: 0.95rem; font-weight: 800; color: #FFFFFF;"></h3>
              </div>
              <p id="t-item2-desc" style="font-size: 0.75rem; color: #94A3B8; margin-top: 0.15rem;"></p>
            </div>
          </div>
          <div style="text-align: right; flex-shrink: 0;">
            <span id="t-price-b1" style="font-size: 0.75rem; color: #64748B; text-decoration: line-through; display: block;"></span>
            <span id="t-free-tag-1" style="font-size: 0.75rem; font-weight: 800; color: #10B981;">GRÁTIS</span>
          </div>
        </div>

        <!-- Item 3 -->
        <div style="padding: 1rem 0; border-bottom: 1px solid #1E2538; display: flex; justify-content: space-between; align-items: flex-start; gap: 0.75rem;">
          <div style="display: flex; gap: 0.75rem; align-items: flex-start;">
            <span style="font-size: 1.25rem;">🎁</span>
            <div>
              <div style="display: flex; align-items: center; gap: 0.35rem;">
                <span id="t-item3-badge" style="background: rgba(245,158,11,0.2); color: #FDE68A; font-size: 0.65rem; font-weight: 800; padding: 0.15rem 0.4rem; border-radius: 0.25rem;">BÔNUS 2</span>
                <h3 id="t-item3-title" style="font-size: 0.95rem; font-weight: 800; color: #FFFFFF;"></h3>
              </div>
              <p id="t-item3-desc" style="font-size: 0.75rem; color: #94A3B8; margin-top: 0.15rem;"></p>
            </div>
          </div>
          <div style="text-align: right; flex-shrink: 0;">
            <span id="t-price-b2" style="font-size: 0.75rem; color: #64748B; text-decoration: line-through; display: block;"></span>
            <span id="t-free-tag-2" style="font-size: 0.75rem; font-weight: 800; color: #10B981;">GRÁTIS</span>
          </div>
        </div>

        <!-- Price Calculation -->
        <div style="padding-top: 1.5rem; text-align: center;">
          <p style="font-size: 0.82rem; color: #94A3B8;">
            <span id="t-total-val-label">Valor Total Acumulado:</span> <span id="t-price-total" style="text-decoration: line-through; color: #64748B; font-weight: 700;"></span>
          </p>
          <div style="margin: 0.5rem 0 1rem 0;">
            <span id="t-promo-price-label" style="font-size: 0.75rem; text-transform: uppercase; font-weight: 800; color: #CBD5E1; display: block;">
              Preço Promocional de Lançamento:
            </span>
            <div id="t-price-big" style="font-size: 2.85rem; font-weight: 900; color: #F59E0B; line-height: 1;"></div>
            <span id="t-payment-type-label" style="font-size: 0.75rem; color: #10B981; font-weight: 700;">Pagamento Único</span>
          </div>

          <!-- DIRECT ACTION BUTTON -->
          <a id="t-cta-offer-btn" href="https://checkout.escalepay.com/1889386" target="_blank" class="btn-gold pulse-glow" style="margin-bottom: 0.75rem;">
            <span id="t-cta-offer">ATIVAR MEU CÓDIGO AGORA</span>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <line x1="5" y1="12" x2="19" y2="12"></line>
              <polyline points="12 5 19 12 12 19"></polyline>
            </svg>
          </a>

          <!-- Payment Methods Info -->
          <div style="background: rgba(0,0,0,0.5); border-radius: 0.75rem; padding: 0.65rem; border: 1px solid #1E2538;">
            <p id="t-secure-proc" style="font-size: 0.7rem; color: #94A3B8; margin-bottom: 0.4rem;"></p>
            <div id="t-payment-methods" style="display: flex; justify-content: center; gap: 0.5rem; font-size: 0.72rem; font-weight: 700; color: #CBD5E1;"></div>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 9. PARA QUEM É / PARA QUEM NÃO É -->
  <!-- ========================================================================= -->
  <section style="background: #0B0E15; border-top: 1px solid #1E2538; border-bottom: 1px solid #1E2538; padding: 3.5rem 0;">
    <div class="container-wide">
      
      <div style="text-align: center; margin-bottom: 2rem;">
        <h2 id="t-compat-title" style="font-size: clamp(1.4rem, 5vw, 1.85rem); text-transform: uppercase; color: #FFFFFF;">
          Aviso de Compatibilidade
        </h2>
        <p id="t-compat-desc" style="font-size: 0.85rem; color: #94A3B8; margin-top: 0.25rem;"></p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem;">
        
        <!-- NÃO É -->
        <div style="background: rgba(239, 68, 68, 0.08); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 1.25rem; padding: 1.5rem;">
          <div style="display: flex; align-items: center; gap: 0.5rem; color: #EF4444; font-weight: 900; font-size: 0.95rem; text-transform: uppercase; margin-bottom: 1rem;">
            <span>✕</span>
            <span id="t-not-for-title">NÃO É PARA QUEM:</span>
          </div>
          <ul style="list-style: none; font-size: 0.82rem; color: #CBD5E1; display: flex; flex-direction: column; gap: 0.75rem;">
            <li style="display: flex; gap: 0.5rem;"><span style="color: #EF4444; font-weight: 800;">•</span><span id="t-not-for-1"></span></li>
            <li style="display: flex; gap: 0.5rem;"><span style="color: #EF4444; font-weight: 800;">•</span><span id="t-not-for-2"></span></li>
            <li style="display: flex; gap: 0.5rem;"><span style="color: #EF4444; font-weight: 800;">•</span><span id="t-not-for-3"></span></li>
          </ul>
        </div>

        <!-- É PARA -->
        <div style="background: rgba(245, 158, 11, 0.08); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 1.25rem; padding: 1.5rem;">
          <div style="display: flex; align-items: center; gap: 0.5rem; color: #F59E0B; font-weight: 900; font-size: 0.95rem; text-transform: uppercase; margin-bottom: 1rem;">
            <span>✓</span>
            <span id="t-for-title">É EXATAMENTE PARA QUEM:</span>
          </div>
          <ul style="list-style: none; font-size: 0.82rem; color: #CBD5E1; display: flex; flex-direction: column; gap: 0.75rem;">
            <li style="display: flex; gap: 0.5rem;"><span style="color: #F59E0B; font-weight: 800;">•</span><span id="t-for-1"></span></li>
            <li style="display: flex; gap: 0.5rem;"><span style="color: #F59E0B; font-weight: 800;">•</span><span id="t-for-2"></span></li>
            <li style="display: flex; gap: 0.5rem;"><span style="color: #F59E0B; font-weight: 800;">•</span><span id="t-for-3"></span></li>
          </ul>
        </div>

      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 10. GARANTIA BLINDADA DE 7 DIAS -->
  <!-- ========================================================================= -->
  <section style="padding: 3.5rem 0;">
    <div class="container-custom">
      
      <div class="glass-card" style="padding: 2rem 1.5rem; text-align: center; border: 1px solid rgba(245,158,11,0.3);">
        <div style="width: 60px; height: 60px; margin: 0 auto 1rem auto; background: linear-gradient(135deg, #F59E0B, #D97706); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.75rem; box-shadow: 0 0 25px rgba(245,158,11,0.4);">
          🛡️
        </div>

        <div id="t-guar-badge" class="badge-pill badge-gold" style="margin-bottom: 0.75rem;">
          RISCO ZERO • GARANTIA TOTAL
        </div>

        <h2 id="t-guar-title" style="font-size: clamp(1.35rem, 5vw, 1.85rem); text-transform: uppercase; color: #FFFFFF; margin-bottom: 0.75rem;">
          7 Dias de Garantia Incondicional
        </h2>

        <p id="t-guar-desc" style="font-size: 0.88rem; color: #CBD5E1; line-height: 1.6; max-width: 480px; margin: 0 auto 1rem auto;"></p>

        <p id="t-guar-bold" style="font-size: 0.82rem; font-weight: 800; color: #F59E0B; text-transform: uppercase;"></p>
      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 11. CTA FINAL -->
  <!-- ========================================================================= -->
  <section style="background: linear-gradient(180deg, #0B0E15 0%, #07080B 100%); padding: 3.5rem 0; text-align: center;">
    <div class="container-custom">
      
      <h2 style="font-size: clamp(1.6rem, 5.5vw, 2.25rem); text-transform: uppercase; color: #FFFFFF; margin-bottom: 0.75rem;">
        <span id="t-final-title">Ninguém vem te salvar.</span> <br />
        <span id="t-final-title-gold" class="gold-gradient-text">A decisão é sua.</span>
      </h2>

      <p id="t-final-desc" style="font-size: 0.9rem; color: #CBD5E1; max-width: 460px; margin: 0 auto 1.75rem auto; line-height: 1.6;"></p>

      <a id="t-final-cta-btn" href="https://checkout.escalepay.com/1889386" target="_blank" class="btn-gold pulse-glow" style="max-width: 480px; margin: 0 auto;">
        <span id="t-final-cta">QUERO MINHA MENTE INABALÁVEL AGORA</span>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <line x1="5" y1="12" x2="19" y2="12"></line>
          <polyline points="12 5 19 12 12 19"></polyline>
        </svg>
      </a>

      <div id="t-final-urgency" style="margin-top: 1.25rem; font-size: 0.72rem; color: #64748B;"></div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 12. FAQ -->
  <!-- ========================================================================= -->
  <section style="background: #080B10; border-top: 1px solid #1E2538; padding: 3.5rem 0;">
    <div class="container-custom">
      
      <div style="text-align: center; margin-bottom: 2rem;">
        <div id="t-faq-badge" class="badge-pill" style="background: #1E2538; color: #CBD5E1; margin-bottom: 0.5rem;">
          DÚVIDAS FREQUENTES
        </div>
        <h2 id="t-faq-title" style="font-size: clamp(1.4rem, 5vw, 1.85rem); text-transform: uppercase; color: #FFFFFF;">
          Perguntas Frequentes
        </h2>
      </div>

      <div id="faqList">
        <div class="faq-item">
          <button class="faq-btn" onclick="toggleFaq(this)">
            <span id="t-faq1-q">1. Como vou receber o e-book e os bônus?</span>
            <span class="faq-icon" style="color: #F59E0B; font-size: 1.25rem;">+</span>
          </button>
          <div id="t-faq1-a" class="faq-body"></div>
        </div>

        <div class="faq-item">
          <button class="faq-btn" onclick="toggleFaq(this)">
            <span id="t-faq2-q">2. Quais são as formas de pagamento?</span>
            <span class="faq-icon" style="color: #F59E0B; font-size: 1.25rem;">+</span>
          </button>
          <div id="t-faq2-a" class="faq-body"></div>
        </div>

        <div class="faq-item">
          <button class="faq-btn" onclick="toggleFaq(this)">
            <span id="t-faq3-q">3. Serve para quem nunca leu nada sobre estoicismo?</span>
            <span class="faq-icon" style="color: #F59E0B; font-size: 1.25rem;">+</span>
          </button>
          <div id="t-faq3-a" class="faq-body"></div>
        </div>

        <div class="faq-item">
          <button class="faq-btn" onclick="toggleFaq(this)">
            <span id="t-faq4-q">4. Quanto tempo do meu dia eu preciso dedicar?</span>
            <span class="faq-icon" style="color: #F59E0B; font-size: 1.25rem;">+</span>
          </button>
          <div id="t-faq4-a" class="faq-body"></div>
        </div>

        <div class="faq-item">
          <button class="faq-btn" onclick="toggleFaq(this)">
            <span id="t-faq5-q">5. Como funciona a garantia de 7 dias?</span>
            <span class="faq-icon" style="color: #F59E0B; font-size: 1.25rem;">+</span>
          </button>
          <div id="t-faq5-a" class="faq-body"></div>
        </div>
      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- FOOTER -->
  <!-- ========================================================================= -->
  <footer style="background: #050608; border-top: 1px solid #141926; padding: 2.5rem 1rem; text-align: center; font-size: 0.75rem; color: #64748B;">
    <div style="max-width: 500px; margin: 0 auto; display: flex; flex-direction: column; gap: 0.75rem;">
      <div style="font-family: 'Cinzel', serif; font-weight: 800; font-size: 0.95rem; color: #94A3B8; letter-spacing: 0.1em; text-transform: uppercase;">
        MENTE INABALÁVEL
      </div>
      <p id="t-footer-desc">
        O Código do Homem Frio, Focado e Implacável • Pagamento e entrega processados com segurança.
      </p>
      <p style="font-size: 0.68rem; color: #475569;">
        Todos os direitos reservados © 2026.
      </p>
    </div>
  </footer>

  <!-- ========================================================================= -->
  <!-- STICKY MOBILE CTA BAR -->
  <!-- ========================================================================= -->
  <div id="stickyBar">
    <div style="display: flex; align-items: center; justify-content: space-between; gap: 0.75rem; max-width: 480px; margin: 0 auto;">
      <div>
        <span style="font-size: 0.65rem; text-transform: uppercase; font-weight: 800; color: #94A3B8; display: block;">Lançamento</span>
        <span id="t-sticky-price" style="font-size: 1.25rem; font-weight: 900; color: #F59E0B;">147MT</span>
      </div>
      <a id="t-sticky-btn-link" href="https://checkout.escalepay.com/1889386" target="_blank" class="btn-gold" style="padding: 0.75rem 1.15rem; font-size: 0.8rem; border-radius: 0.75rem; width: auto; flex: 1;">
        <span id="t-sticky-btn">COMPRAR AGORA</span>
      </a>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- JAVASCRIPT LOGIC & REACTIVE TRANSLATIONS -->
  <!-- ========================================================================= -->
  <script>
    const i18n = TRANSLATIONS_JSON_PLACEHOLDER;
    let currentCountry = 'MZ';

    function setContent(id, html) {
      const el = document.getElementById(id);
      if (el) el.innerHTML = html;
    }

    function selectCountry(countryCode) {
      if (!i18n[countryCode]) return;
      currentCountry = countryCode;
      localStorage.setItem('user_country_choice', countryCode);
      document.getElementById('countryModal').style.display = 'none';

      // Update Header Switcher active state
      ['MZ', 'BR', 'US', 'ES'].forEach(c => {
        const btn = document.getElementById('btn-' + c);
        if (btn) {
          if (c === countryCode) btn.classList.add('active');
          else btn.classList.remove('active');
        }
      });

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
    }

    // Initialize country from storage or show modal on first visit
    window.addEventListener('DOMContentLoaded', () => {
      const saved = localStorage.getItem('user_country_choice');
      if (saved && i18n[saved]) {
        selectCountry(saved);
      } else {
        // Show modal selector on first visit
        document.getElementById('countryModal').style.display = 'flex';
        selectCountry('MZ'); // default
      }
    });

    // Countdown Timer
    let totalSeconds = 14 * 60 + 59;
    const countdownEl = document.getElementById('countdown');
    function updateCountdown() {
      const minutes = Math.floor(totalSeconds / 60);
      const seconds = totalSeconds % 60;
      countdownEl.textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
      if (totalSeconds > 0) totalSeconds--;
      else totalSeconds = 15 * 60;
    }
    setInterval(updateCountdown, 1000);
    updateCountdown();

    // Quiz Logic
    const quizState = { 1: null, 2: null, 3: null };
    function selectQuiz(qNum, choice, el) {
      const parent = el.parentElement;
      const options = parent.querySelectorAll('.quiz-option');
      options.forEach(opt => {
        opt.classList.remove('selected-weak', 'selected-strong');
        const circle = opt.querySelector('.radio-circle');
        circle.textContent = '';
        circle.style.borderColor = '#475569';
        circle.style.background = 'transparent';
      });

      const circle = el.querySelector('.radio-circle');
      if (choice === 'weak') {
        el.classList.add('selected-weak');
        circle.textContent = '✕';
        circle.style.borderColor = '#EF4444';
        circle.style.background = '#EF4444';
        circle.style.color = '#FFFFFF';
      } else {
        el.classList.add('selected-strong');
        circle.textContent = '✓';
        circle.style.borderColor = '#F59E0B';
        circle.style.background = '#F59E0B';
        circle.style.color = '#07080B';
      }

      quizState[qNum] = choice;
      if (quizState[1] && quizState[2] && quizState[3]) {
        const feedback = document.getElementById('quizFeedback');
        feedback.style.display = 'block';
        feedback.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }

    // FAQ
    function toggleFaq(btn) {
      const body = btn.nextElementSibling;
      const icon = btn.querySelector('.faq-icon');
      const isOpen = body.classList.contains('open');

      document.querySelectorAll('.faq-body').forEach(b => b.classList.remove('open'));
      document.querySelectorAll('.faq-icon').forEach(i => i.textContent = '+');

      if (!isOpen) {
        body.classList.add('open');
        icon.textContent = '−';
      }
    }

    // Sticky Bar
    const stickyBar = document.getElementById('stickyBar');
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) stickyBar.classList.add('visible');
      else stickyBar.classList.remove('visible');
    });
  </script>

</body>
</html>
"""

final_html = html_code.replace("IMAGE_EBOOK_PLACEHOLDER", b64_ebook)
final_html = final_html.replace("IMAGE_BUNDLE_PLACEHOLDER", b64_bundle)
final_html = final_html.replace("IMAGE_HERO_PLACEHOLDER", b64_hero)
final_html = final_html.replace("TRANSLATIONS_JSON_PLACEHOLDER", json.dumps(translations, ensure_ascii=False))

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Successfully built Global Multilingual Sales Page (BR, US, ES, MZ)! Size:", os.path.getsize('/home/user/index.html'))
