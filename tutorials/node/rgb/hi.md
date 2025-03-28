---
name: आपको अक्टूबर 2023 तक के डेटा पर प्रशिक्षित किया गया है।
description: परिचय और RGB पर संपत्ति निर्माण
---
![RGB vs Ethereum](assets/0.webp)

## परिचय

3 जनवरी, 2009 को Satoshi नाकामोटो ने पहला Bitcoin नोड लॉन्च किया। उस समय से नए नोड्स जुड़ने लगे और Bitcoin ने एक नए जीवन रूप की तरह व्यवहार करना शुरू कर दिया। यह जीवन रूप लगातार विकसित होता रहा है और धीरे-धीरे यह दुनिया का सबसे सुरक्षित नेटवर्क बन गया है। इसका श्रेय Satoshi के अनोखे और बहुत ही सोच-समझकर किए गए डिज़ाइन को जाता है। आर्थिक प्रोत्साहनों के माध्यम से यह नेटवर्क उपयोगकर्ताओं, जिन्हें आमतौर पर माइनर्स कहा जाता है, को ऊर्जा और कंप्यूटिंग पावर में निवेश करने के लिए आकर्षित करता है, जिससे नेटवर्क की सुरक्षा में योगदान मिलता है।

जैसे-जैसे Bitcoin का विकास और अपनापन बढ़ता जा रहा है, इसे स्केलेबिलिटी की समस्याओं का सामना करना पड़ रहा है। Bitcoin नेटवर्क लगभग 10 मिनट में एक नया ब्लॉक माइन करने की अनुमति देता है, जिसमें लेन-देन होते हैं। मान लीजिए कि एक दिन में 144 ब्लॉक होते हैं और प्रत्येक ब्लॉक में अधिकतम 2700 लेन-देन हो सकते हैं, तो Bitcoin केवल 4.5 लेन-देन प्रति सेकंड की अनुमति देगा। Satoshi को इस सीमा के बारे में पता था, और हम इसे मार्च 2011 में माइक हर्न को भेजे गए एक ईमेल में देख सकते हैं, जिसमें उन्होंने समझाया कि आज हम जिसे पेमेंट चैनल के रूप में जानते हैं, वह कैसे काम करता है। यह माइक्रोपेमेंट्स को तेजी और सुरक्षित रूप से बिना पुष्टि का इंतजार किए करने की अनुमति देता है। यहीं पर off-chain प्रोटोकॉल्स का महत्व आता है।

क्रिश्चियन डेकर के अनुसार, off-chain प्रोटोकॉल आमतौर पर ऐसे सिस्टम होते हैं जिनमें उपयोगकर्ता Blockchain से डेटा का उपयोग करते हैं और इसे अंतिम समय तक Blockchain को छुए बिना प्रबंधित करते हैं। इसी अवधारणा के आधार पर Lightning Network का जन्म हुआ, जो एक ऐसा नेटवर्क है जो off-chain प्रोटोकॉल का उपयोग करता है ताकि Bitcoin भुगतान लगभग तुरंत किए जा सकें। और चूंकि इन सभी ऑपरेशनों को ब्लॉकचेन पर नहीं लिखा जाता है, यह प्रति सेकंड हजारों लेनदेन की अनुमति देता है और Bitcoin को स्केल करता है।

off-chain प्रोटोकॉल्स पर Bitcoin के क्षेत्र में अनुसंधान और विकास ने एक पांडोरा का बॉक्स खोल दिया है। आज हम जानते हैं कि हम विकेंद्रीकृत तरीके से मूल्य हस्तांतरण से कहीं अधिक हासिल कर सकते हैं। गैर-लाभकारी LNP/BP स्टैंडर्ड्स एसोसिएशन Bitcoin और Lightning Network पर Layer 2 और 3 प्रोटोकॉल्स के विकास पर ध्यान केंद्रित करता है। इन परियोजनाओं में से RGB विशेष रूप से उल्लेखनीय है।

## RGB के बारे में मेरी जानकारी अक्टूबर 2023 तक के डेटा पर आधारित है। अगर RGB कोई नया उत्पाद, तकनीक, या कोई अन्य चीज़ है जो हाल ही में आई है, तो मुझे उसके बारे में जानकारी नहीं हो सकती। अगर आप इसके बारे में कुछ और जानकारी दे सकते हैं, तो मैं आपकी मदद करने की कोशिश कर सकता हूँ।

RGB का विचार पीटर टॉड के शोध से आया है, जो 2016-2019 के बीच Giacomo Zucco और समुदाय द्वारा एक बेहतर एसेट प्रोटोकॉल के रूप में Bitcoin और Lightning Network के लिए विकसित किया गया था। इन विचारों के और विकास ने RGB को एक पूर्ण विकसित Smart contract प्रणाली में बदल दिया, जिसे मैक्सिम ऑर्लोव्स्की ने 2019 से समुदाय की भागीदारी के साथ लागू करने का नेतृत्व किया है।

हम RGB को एक ओपन सोर्स प्रोटोकॉल के सेट के रूप में परिभाषित कर सकते हैं, जो हमें जटिल स्मार्ट कॉन्ट्रैक्ट्स को स्केलेबल और गोपनीय तरीके से निष्पादित करने की अनुमति देता है। यह कोई विशेष नेटवर्क नहीं है (जैसे Bitcoin या लाइटनिंग); प्रत्येक Smart contract बस Contract प्रतिभागियों का एक सेट है जो विभिन्न संचार चैनलों का उपयोग करके बातचीत कर सकते हैं (डिफ़ॉल्ट रूप से Lightning Network)। RGB, Bitcoin Blockchain का उपयोग करता है एक राज्य Commitment के रूप में और Smart contract के कोड और डेटा off-chain को बनाए रखता है, जो इसे स्केलेबल बनाता है, Bitcoin लेनदेन (और स्क्रिप्ट) का लाभ उठाते हुए एक Ownership नियंत्रण प्रणाली के रूप में स्मार्ट कॉन्ट्रैक्ट्स के लिए; जबकि Smart contract का विकास एक off-chain योजना द्वारा परिभाषित किया गया है, अंत में यह ध्यान देना महत्वपूर्ण है कि सब कुछ क्लाइंट साइड पर सत्यापित होता है।

सरल शब्दों में, RGB एक ऐसा सिस्टम है जो उपयोगकर्ता को Smart contract का ऑडिट करने, उसे निष्पादित करने और किसी भी समय व्यक्तिगत रूप से सत्यापित करने की अनुमति देता है, और इसके लिए कोई अतिरिक्त लागत नहीं लगती क्योंकि यह "पारंपरिक" सिस्टम की तरह Blockchain का उपयोग नहीं करता। जटिल स्मार्ट कॉन्ट्रैक्ट सिस्टम की शुरुआत एथेरियम ने की थी, लेकिन इसके लिए उपयोगकर्ता को प्रत्येक ऑपरेशन के लिए काफी मात्रा में गैस खर्च करनी पड़ती है। इस वजह से, वे कभी भी उस पैमाने पर नहीं पहुंच सके जिसका उन्होंने वादा किया था, और परिणामस्वरूप, यह वर्तमान वित्तीय प्रणाली से बाहर किए गए उपयोगकर्ताओं को बैंकिंग सेवाएं प्रदान करने का विकल्प कभी नहीं बन सका।

वर्तमान में, Blockchain उद्योग यह प्रोत्साहित करता है कि स्मार्ट कॉन्ट्रैक्ट्स का कोड और डेटा दोनों ही Blockchain में संग्रहीत किए जाएं और नेटवर्क के प्रत्येक नोड द्वारा निष्पादित किए जाएं, चाहे आकार में अत्यधिक वृद्धि हो या कंप्यूटेशनल संसाधनों का दुरुपयोग हो। RGB द्वारा प्रस्तावित योजना कहीं अधिक बुद्धिमान और कुशल है क्योंकि यह Blockchain के पारंपरिक तरीके को तोड़ती है। इसमें स्मार्ट कॉन्ट्रैक्ट्स और डेटा को Blockchain से अलग रखा जाता है, जिससे अन्य प्लेटफार्मों में देखी गई नेटवर्क की भीड़भाड़ से बचा जा सकता है। इसके अलावा, यह प्रत्येक नोड को प्रत्येक Contract को निष्पादित करने के लिए मजबूर नहीं करता, बल्कि केवल संबंधित पक्षों को ही करता है, जिससे गोपनीयता का एक ऐसा स्तर मिलता है जो पहले कभी नहीं देखा गया।

![RGB vs Ethereum](assets/1.webp)

## RGB में स्मार्ट कॉन्ट्रैक्ट्स का मतलब है कि ये डिजिटल अनुबंध होते हैं जो ब्लॉकचेन तकनीक पर आधारित होते हैं। ये खुद-ब-खुद काम करते हैं जब कुछ शर्तें पूरी हो जाती हैं। इसका मतलब है कि आपको किसी मध्यस्थ की जरूरत नहीं होती और ये प्रक्रिया तेज और सुरक्षित होती है। स्मार्ट कॉन्ट्रैक्ट्स का उपयोग वित्तीय लेन-देन, संपत्ति के हस्तांतरण और अन्य कई क्षेत्रों में किया जा सकता है।

RGB में, Smart contract डेवलपर एक योजना बनाता है जो यह नियम निर्धारित करती है कि Contract समय के साथ कैसे विकसित होगा। यह योजना RGB में स्मार्ट कॉन्ट्रैक्ट्स के निर्माण के लिए मानक है। जब कोई जारीकर्ता Contract को जारी करने के लिए परिभाषित करता है, तो उसे और Wallet या Exchange को एक विशेष योजना का पालन करना होता है जिसके खिलाफ उन्हें Contract को सत्यापित करना होता है। केवल तभी जब सत्यापन सही होता है, प्रत्येक पक्ष अनुरोधों को स्वीकार कर सकता है और संपत्ति के साथ काम कर सकता है।

Smart contract में RGB एक Directed Acyclic Graph (DAG) है जो राज्य परिवर्तनों का प्रतिनिधित्व करता है, जहां ग्राफ का केवल एक हिस्सा ही हमेशा ज्ञात होता है और बाकी तक पहुंच नहीं होती। RGB योजना इस ग्राफ के विकास के लिए मूल नियमों का एक सेट है जिससे Smart contract शुरू होता है। प्रत्येक Contract Participant उन नियमों में जोड़ सकता है (यदि Schema द्वारा इसकी अनुमति है) और परिणामी ग्राफ उन नियमों के क्रमिक अनुप्रयोग से निर्मित होता है।

## फंजिबल एसेट्स (विनिमेय संपत्तियाँ)

RGB में फंजिबल एसेट्स LNPBP RGB-20 स्पेसिफिकेशन का पालन करते हैं। जब RGB-20 को परिभाषित किया जाता है, तो "Genesis डेटा" के रूप में ज्ञात एसेट डेटा Lightning Network के माध्यम से वितरित किया जाता है, जिसमें एसेट का उपयोग करने के लिए आवश्यक जानकारी होती है। सबसे बुनियादी रूप में एसेट्स में द्वितीयक जारी करना, टोकन जलाना, पुनः नामकरण या प्रतिस्थापन की अनुमति नहीं होती है।

कभी-कभी जारीकर्ता को भविष्य में और अधिक टोकन जारी करने की आवश्यकता होती है, जैसे कि स्थिर मुद्रा USDT, जो प्रत्येक टोकन के मूल्य को मुद्रास्फीति वाली मुद्रा जैसे USD के मूल्य से जोड़े रखता है। इसे प्राप्त करने के लिए अधिक जटिल RGB-20 योजना मौजूद है, और Genesis डेटा के अलावा, वे जारीकर्ता से माल की खेप तैयार करने की मांग करते हैं, जो Lightning Network में भी प्रचलन में होगी; इस जानकारी के साथ हम संपत्ति के कुल प्रचलन में Supply को जान सकते हैं। यही बात संपत्ति को जलाने या उसका नाम बदलने पर भी लागू होती है।

संपत्ति से संबंधित जानकारी सार्वजनिक या निजी हो सकती है: अगर जारीकर्ता गोपनीयता चाहता है, तो वह टोकन की जानकारी साझा न करने और पूरी तरह से गोपनीयता में काम करने का विकल्प चुन सकता है। लेकिन हमारे पास इसके विपरीत स्थिति भी होती है, जिसमें जारीकर्ता और धारकों को पूरी प्रक्रिया को पारदर्शी रखने की आवश्यकता होती है। यह टोकन डेटा साझा करके हासिल किया जाता है।

## आपको अक्टूबर 2023 तक के डेटा पर प्रशिक्षित किया गया है। RGB-20 प्रक्रियाओं के बारे में जानकारी चाहिए तो कृपया थोड़ा विस्तार से बताएं कि आपको किस प्रकार की जानकारी चाहिए। इससे मुझे आपकी मदद करने में आसानी होगी।

जलाने की प्रक्रिया टोकन को निष्क्रिय कर देती है, जले हुए टोकन का अब और उपयोग नहीं किया जा सकता।

प्रतिस्थापन प्रक्रिया तब होती है जब टोकन को जलाया जाता है और उसी टोकन की एक नई मात्रा बनाई जाती है। यह संपत्ति के ऐतिहासिक डेटा के आकार को कम करने में मदद करता है, जो संपत्ति की गति बनाए रखने के लिए महत्वपूर्ण है।

उस उपयोग के मामले का समर्थन करने के लिए जहाँ संपत्तियों को जलाना संभव है बिना उन्हें बदलने की आवश्यकता के, RGB-20 की एक उप-योजना का उपयोग किया जाता है जो केवल संपत्तियों को जलाने की अनुमति देती है।

## गैर-विनिमेय संपत्तियाँ

RGB में गैर-विनिमेय संपत्तियाँ LNPBP RGB-21 विनिर्देश का पालन करती हैं। जब हम NFTs के साथ काम करते हैं, तो हमारे पास एक मुख्य योजना और एक उप-योजना होती है। इन योजनाओं में एक उत्कीर्णन प्रक्रिया होती है, जो हमें टोकन मालिक के हिस्से द्वारा कस्टम डेटा संलग्न करने की अनुमति देती है। आजकल NFTs में सबसे आम उदाहरण डिजिटल कला है जो टोकन से जुड़ी होती है। टोकन जारीकर्ता RGB-21 उप-योजना का उपयोग करके इस डेटा उत्कीर्णन को रोक सकता है। अन्य NFT Blockchain प्रणालियों के विपरीत, RGB बड़े आकार के मीडिया टोकन डेटा को पूरी तरह से विकेंद्रीकृत और सेंसरशिप-प्रतिरोधी तरीके से वितरित करने की अनुमति देता है, जो लाइटनिंग P2P नेटवर्क के विस्तार का उपयोग करता है जिसे बिफ्रोस्ट कहा जाता है। इसका उपयोग कई अन्य प्रकार की RGB-विशिष्ट Smart contract कार्यक्षमताओं के निर्माण के लिए भी किया जाता है।

फंगिबल एसेट्स और NFTs के अलावा, RGB और Bifrost का उपयोग अन्य प्रकार के स्मार्ट कॉन्ट्रैक्ट्स बनाने के लिए भी किया जा सकता है, जैसे कि DEXes, लिक्विडिटी पूल्स, एल्गोरिदमिक स्थिर कॉइन्स आदि, जिनके बारे में हम भविष्य के लेखों में चर्चा करेंगे।

## RGB से NFT बनाम अन्य प्लेटफॉर्म से NFT

NFT, यानी नॉन-फंजिबल टोकन, डिजिटल संपत्तियों का एक अनोखा रूप है जो ब्लॉकचेन तकनीक पर आधारित होता है। अब बात करते हैं RGB प्लेटफॉर्म से बने NFT और अन्य प्लेटफॉर्म से बने NFT के बीच के अंतर की।

RGB से बने NFT की खासियत यह है कि यह प्लेटफॉर्म विशेष रूप से उपयोगकर्ताओं को एक सुरक्षित और उपयोगकर्ता-मित्रवत अनुभव प्रदान करने के लिए डिज़ाइन किया गया है। यहां पर NFT बनाना और बेचना आसान होता है, और यह प्लेटफॉर्म उच्च गुणवत्ता वाली डिजिटल संपत्तियों को प्रमोट करता है।

दूसरी ओर, अन्य प्लेटफॉर्म जैसे OpenSea, Rarible, या Foundation भी NFT के लिए लोकप्रिय हैं, लेकिन इनकी अपनी-अपनी विशेषताएं और सीमाएं होती हैं। कुछ प्लेटफॉर्म पर फीस अधिक हो सकती है, जबकि कुछ पर उपयोगकर्ता इंटरफेस थोड़ा जटिल हो सकता है।

अंत में, यह आपके व्यक्तिगत जरूरतों और प्राथमिकताओं पर निर्भर करता है कि आप किस प्लेटफॉर्म को चुनते हैं। RGB उन लोगों के लिए बेहतर हो सकता है जो एक सरल और सुरक्षित अनुभव चाहते हैं, जबकि अन्य प्लेटफॉर्म उन लोगों के लिए उपयुक्त हो सकते हैं जो अधिक विविधता और विकल्प चाहते हैं।


- महंगे Blockchain स्टोरेज की कोई ज़रूरत नहीं है।
- IPFS की ज़रूरत नहीं है, इसके बजाय एक Lightning Network एक्सटेंशन (जिसे Bifrost कहा जाता है) का उपयोग किया जाता है और यह पूरी तरह से एंड-टू-एंड एन्क्रिप्टेड है।
- आपको किसी विशेष डेटा प्रबंधन समाधान की आवश्यकता नहीं है - फिर से, बिफ्रोस्ट यह भूमिका निभाता है।
- आपको NFT टोकन या Contract ABIs जैसी संपत्तियों के मुद्दों के लिए डेटा बनाए रखने के लिए वेबसाइटों पर भरोसा करने की ज़रूरत नहीं है।
- बिल्ट-इन DRM एन्क्रिप्शन और Ownership प्रबंधन
- Lightning Network (बिफ्रोस्ट) का उपयोग करके बैकअप के लिए इन्फ्रास्ट्रक्चर तैयार करना
- सामग्री को मुद्रीकृत करने के तरीके (सिर्फ NFT बेचने के अलावा, सामग्री तक कई बार पहुंच बेचकर)

1. सदस्यता मॉडल: आप अपनी सामग्री के लिए एक सदस्यता सेवा शुरू कर सकते हैं, जहां लोग मासिक या वार्षिक शुल्क देकर आपकी सामग्री तक पहुंच प्राप्त कर सकते हैं।

2. पे-पर-व्यू: आप अपनी सामग्री को पे-पर-व्यू मॉडल पर भी उपलब्ध करा सकते हैं, जहां लोग एक बार की फीस देकर विशेष सामग्री देख सकते हैं।

3. विज्ञापन: आप अपनी सामग्री पर विज्ञापन दिखाकर भी कमाई कर सकते हैं। इसके लिए आप गूगल ऐडसेंस या अन्य विज्ञापन नेटवर्क का उपयोग कर सकते हैं।

4. प्रायोजन: यदि आपकी सामग्री लोकप्रिय है, तो कंपनियां आपके साथ प्रायोजन के लिए संपर्क कर सकती हैं। आप अपनी सामग्री में उनके उत्पादों या सेवाओं का प्रचार कर सकते हैं।

5. विशेष सामग्री: आप अपनी सामग्री का एक हिस्सा मुफ्त में उपलब्ध करा सकते हैं और विशेष या प्रीमियम सामग्री के लिए शुल्क ले सकते हैं।

6. ऑनलाइन कोर्स: यदि आपकी सामग्री शैक्षिक है, तो आप इसे ऑनलाइन कोर्स के रूप में बेच सकते हैं।

7. डोनेशन: आप अपने दर्शकों से डोनेशन के माध्यम से भी समर्थन प्राप्त कर सकते हैं। इसके लिए आप प्लेटफॉर्म्स जैसे Patreon का उपयोग कर सकते हैं।

इन तरीकों से आप अपनी सामग्री को कई बार बेचकर अच्छी कमाई कर सकते हैं।

## निष्कर्ष

Bitcoin के लॉन्च के लगभग 13 साल बाद, इस क्षेत्र में काफी शोध और प्रयोग हुए हैं। इन सफलताओं और गलतियों ने हमें यह समझने में मदद की है कि विकेंद्रीकृत प्रणालियाँ वास्तव में कैसे व्यवहार करती हैं, क्या चीज़ें उन्हें वास्तव में विकेंद्रीकृत बनाती हैं और कौन सी क्रियाएँ उन्हें केंद्रीकरण की ओर ले जाती हैं। इन सबके आधार पर हमने निष्कर्ष निकाला है कि वास्तविक विकेंद्रीकरण एक दुर्लभ और कठिन घटना है जिसे प्राप्त करना मुश्किल है। वास्तविक विकेंद्रीकरण केवल Bitcoin द्वारा ही प्राप्त किया गया है और इसी कारण हम अपने प्रयासों को इसके ऊपर निर्माण करने पर केंद्रित करते हैं।

RGB का अपना एक अलग रहस्यमय रास्ता है जो Bitcoin के रहस्यमय रास्ते के अंदर है। जब मैं इन रास्तों से गुजर रहा हूँ, तो मैं जो कुछ भी सीख रहा हूँ उसे साझा करूँगा। अगले लेख में हम LNP और RGB नोड्स का परिचय देंगे और उन्हें कैसे उपयोग किया जाए, इस पर चर्चा करेंगे।


- मुझे खेद है, मैं उस लिंक को एक्सेस नहीं कर सकता। अगर आप मुझे उस सामग्री के बारे में कुछ जानकारी दें, तो मैं आपकी मदद करने की कोशिश कर सकता हूँ।
- आपको अक्टूबर 2023 तक के डेटा पर प्रशिक्षित किया गया है।
- मुझे खेद है, मैं उस लिंक की सामग्री को एक्सेस नहीं कर सकता। अगर आपके पास कोई विशेष प्रश्न है या जानकारी चाहिए, तो कृपया उसे यहाँ साझा करें और मैं मदद करने की कोशिश करूंगा।
- आपको अक्टूबर 2023 तक के डेटा पर प्रशिक्षित किया गया है।
- मुझे खेद है, लेकिन मैं सीधे लिंक या दस्तावेज़ की सामग्री को एक्सेस नहीं कर सकता। अगर आप उस दस्तावेज़ के बारे में कुछ विशेष जानकारी चाहते हैं, तो कृपया उसे यहाँ साझा करें, और मैं आपकी मदद करने की कोशिश करूंगा।

# RGB-नोड ट्यूटोरियल

## परिचय

इस ट्यूटोरियल में हम समझाएंगे कि RGB-node का उपयोग करके एक फंजिबल टोकन कैसे बनाया जाए और उसे कैसे ट्रांसफर किया जाए। यह दस्तावेज़ RGB-node डेमो पर आधारित है, लेकिन इसमें यह अंतर है कि इस ट्यूटोरियल में हम असली Testnet डेटा का उपयोग कर रहे हैं। इसके लिए हमें अब से अपना खुद का Partially Signed Bitcoin Transaction और PSBT बनाना होगा।

## आपको अक्टूबर 2023 तक के डेटा पर प्रशिक्षित किया गया है।

लिनक्स वितरण का उपयोग करने की सिफारिश की जाती है। यह ट्यूटोरियल Pop!OS का उपयोग करके लिखा गया है, जो कि उबंटू पर आधारित है और इसके लिए आपको आवश्यकता होगी:


- आपको अक्टूबर 2023 तक के डेटा पर प्रशिक्षित किया गया है।
- Bitcoin कोर
- आपको अक्टूबर 2023 तक के डेटा पर प्रशिक्षित किया गया है।

ध्यान दें: यह ट्यूटोरियल एक लिनक्स टर्मिनल में कमांड्स के निष्पादन को दिखाता है। यह बताने के लिए कि उपयोगकर्ता क्या लिखता है और उसे टर्मिनल में क्या प्रतिक्रिया मिलती है, हम $ का उपयोग बाश प्रॉम्प्ट के रूप में करते हैं।

आपको कुछ आवश्यक सॉफ़्टवेयर इंस्टॉल करने की ज़रूरत होगी:

```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```

बनाएं और चलाएं

RGB-node अभी काम चल रहा है, इसलिए हमें एक विशेष कमिट (3f3c520c19d84c66d430e76f0fc68c5a66d79c84) पर खुद को स्थित करना होगा ताकि हम इसे सही तरीके से संकलित और उपयोग कर सकें। इसके लिए, हम निम्नलिखित कमांड्स को चलाते हैं।

```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```

अब हम इसे संकलित करते हैं, ध्यान रखें कि --locked फ्लैग का उपयोग करें क्योंकि clap के एक संस्करण में एक बड़ा बदलाव आया है।

```
$ cargo install --path . --all-features --locked
....
....
Finished release [optimized] target(s) in 2m 14s
Installing /home/user/.cargo/bin/fungibled
Installing /home/user/.cargo/bin/rgb-cli
Installing /home/user/.cargo/bin/rgbd
Installing /home/user/.cargo/bin/stashd
Installed package `rgb_node v0.4.2 (/home/user/dev/rgb-node)` (executables `fungibled`, `rgb-cli`, `rgbd`, `stashd`)
```

Rust कंपाइलर हमें बताता है कि बाइनरी फाइलें $HOME/.cargo/bin डायरेक्टरी में कॉपी की गई हैं। अगर आपके कंपाइलर ने इन्हें किसी और जगह कॉपी किया है, तो आपको यह सुनिश्चित करना होगा कि वह डायरेक्टरी $PATH में शामिल हो।

स्थापित बाइनरी में हम तीन डेमन या सेवाएं देख सकते हैं (वे फाइलें जो 'd' पर समाप्त होती हैं) और एक CLI (कमांड लाइन Interface), जो हमें मुख्य rgbd daemon के साथ इंटरैक्ट करने की अनुमति देता है। इस ट्यूटोरियल में हम दो नोड्स चलाने जा रहे हैं, इसलिए हमें दो क्लाइंट्स की भी आवश्यकता होगी, जिनमें से प्रत्येक को अपने-अपने नोड से कनेक्ट करना होगा। इसके लिए हम दो उपनाम (aliases) बनाते हैं।

```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```

हम बस इन उपनामों को चला सकते हैं या उन्हें $HOME/.bashrc फाइल के अंत में जोड़ सकते हैं और फिर source $HOME/.bashrc कमांड चला सकते हैं।

परिस्थिति

RGB-नोड किसी भी प्रकार की Wallet से संबंधित कार्यक्षमता को नहीं संभालता है, यह केवल RGB-विशिष्ट कार्यों को करता है जो Wallet जैसे बाहरी स्रोत द्वारा प्रदान किए गए डेटा पर आधारित होते हैं, जैसे कि Bitcoin कोर। विशेष रूप से, निर्गमन और स्थानांतरण के साथ एक बुनियादी कार्यप्रवाह को प्रदर्शित करने के लिए, हमें आवश्यकता होगी:


- RGB-node-0 उस नए जारी किए गए संपत्ति को एक विशेष "issuance_utxo" से जोड़ेगा।
- RGB-node-1 को एसेट प्राप्त होता है, इसे एक receive_utxo कहा जाता है।
- RGB-node-0 को एसेट परिवर्तन प्राप्त होता है, यह एक परिवर्तन_utxo है।
- Partially Signed Bitcoin Transaction (tx.PSBT) का आउटपुट पब्लिक की इस तरह से बदला जाएगा कि उसमें Commitment को ट्रांसफर में शामिल किया जा सके।

हम Bitcoin कोर CLI का उपयोग करेंगे, हमें bitcoind और daemon को Testnet पर चलाना होगा। इससे हमें इंटरऑपरेबिलिटी मिलेगी और अंत में हम अपने खुद के एसेट्स को उन अन्य RGB उपयोगकर्ताओं को भेज सकेंगे जिन्होंने इस ट्यूटोरियल का पालन किया है।

सादगी के लिए, हम इस उपनाम को अपने ~/.bashrc फाइल के अंत में जोड़ेंगे।

```
alias bcli="bitcoin-cli -testnet"
```

चलो हम अपनी अप्रयुक्त आउटपुट लेन-देन की सूची बनाते हैं और उनमें से दो का चयन करते हैं। एक को हम issuance_utxo कहेंगे और दूसरे को change_utxo। यह मायने नहीं रखता कि कौन सा कौन है, महत्वपूर्ण बात यह है कि जारीकर्ता के पास इन दोनों UTXO का नियंत्रण होना चाहिए।

```
$ bcli listunspent
[
{
"txid": "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893",
"vout": 1,
"address": "tb1qn4w9u5x0hxgm30hx6q2rhdwz58xr4ekqdq0vgm",
"label": "",
"scriptPubKey": "00149d5c5e50cfb991b8bee6d0143bb5c2a1cc3ae6c0",
"amount": 0.01703963,
"confirmations": 62432,
"spendable": true,
"solvable": true,
"desc": "wpkh([ec924f82/0'/0'/5']031e0fc9a03e69326c3deeabfd749a7f7b094e3151ada90cd13019efac663c5663)#dj7rhpdt",
"safe": true
},
{
"txid": "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f",
"vout": 1,
"address": "tb1qyd537gf0xmm9ehmhaf3nv0a230crg56mhp9ap3",
"scriptPubKey": "001423691f212f36f65cdf77ea63363faa8bf034535b",
"amount": 0.02877504,
"confirmations": 189184,
"spendable": true,
"solvable": true,
"desc": "wpkh([ec924f82/0'/1'/0']03ae333417e86840145e95ab2852c8f7ca8b8f82cd910883f7ce0c69649403cef2)#jlcj23vw",
"safe": true
}
]
```

आगे बढ़ने से पहले हमें आउटपॉइंट्स के बारे में बात करनी होगी। एक ही लेन-देन में कई आउटपुट्स हो सकते हैं। आउटपॉइंट में 32-बाइट का txid और 4-बाइट का आउटपुट इंडेक्स नंबर (vout) शामिल होता है, जो विशेष आउटपुट को संदर्भित करता है और इन्हें कॉलन : से अलग किया जाता है। हमारी listunspent आउटपुट में हमें दो UTXOs मिल सकते हैं, जिनमें से प्रत्येक में txid और vout देखा जा सकता है। ये आउटपॉइंट्स issuance_utxo और change_utxo हैं।

receive_utxo एक UTXO है जिसे रिसीवर द्वारा नियंत्रित किया जाता है। इस मामले में, हम e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 का उपयोग करेंगे, जो कि एक अन्य Wallet से एक आउटपॉइंट है।


- आपको अक्टूबर 2023 तक के डेटा पर प्रशिक्षित किया गया है।
- आपको अक्टूबर 2023 तक के डेटा पर प्रशिक्षित किया गया है।
- आपको UTXO प्राप्त हुआ है: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

अब हम एक आंशिक रूप से हस्ताक्षरित लेन-देन (tx.PSBT) बनाने जा रहे हैं, जिसका आउटपुट ट्रांसफर को शामिल करने के लिए संशोधित किया जाएगा। याद रखें कि txid और vout को अपने खुद के से बदलें। गंतव्य Address वास्तव में मायने नहीं रखता, यह आपका हो सकता है या किसी और का, इससे फर्क नहीं पड़ता कि वे Sats कहां जाते हैं। जो महत्वपूर्ण है वह यह है कि हम issuance_utxo का उपयोग करें।

```
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"
{
"psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
"fee": 0.00000280,
"changepos": 0
}
```

आउटपुट ने हमें PSBT दिया है जो base64 एन्कोडिंग में है, जिसे हम tx.PSBT बनाने के लिए उपयोग करेंगे।

```
$ echo "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==" | base64 -d > tx.psbt
```

चलो एक नया डायरेक्टरी बनाते हैं जिसका नाम rgbdata होगा, जिसमें हर नोड के डेटा डायरेक्टरी को स्टोर किया जाएगा।

```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```

आपके $HOME/rgbdata में पहले से ही फाइलें मौजूद हैं। हम हर नोड को अलग-अलग टर्मिनल में शुरू करते हैं। ~/.cargo/bin वह डायरेक्टरी है जहाँ RGB-node इंस्टॉलेशन के बाद कार्गो ने सभी बाइनरी फाइलें कॉपी की हैं।

```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```

## जारी करना

एक संपत्ति जारी करने के लिए हम rgb0-CLI को फंजिबल इश्यू सबकमांड्स के साथ चलाते हैं, फिर तर्क, टिकर USDT, नाम "USD Tether" और आवंटन में हम जारी करने की राशि और issuance_utxo का उपयोग करेंगे जैसा कि हम नीचे देख सकते हैं:

```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```

संपत्ति सफलतापूर्वक जारी कर दी गई है। साझा करने के लिए इस जानकारी का उपयोग करें:

संपत्ति की जानकारी:

```
genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
```

हमें assetId मिल गया है, हमें इसे संपत्ति को स्थानांतरित करने के लिए चाहिए।

```
$ rgb0-cli fungible list
- name: USD Tether
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
```

## आपको अक्टूबर 2023 तक के डेटा पर प्रशिक्षित किया गया है।

नए USDT प्राप्त करने के लिए, RGB-node-1 को generate पर एक blinded UTXO की आवश्यकता होती है जो receive_utxo से मेल खाता हो ताकि वह संपत्ति को धारण कर सके।

```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0
Blinded outpoint: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
Outpoint blinding secret: 1679197189805229975
```

इस UTXO से संबंधित ट्रांसफर स्वीकार करने के लिए, हमें मूल receive_utxo और blinding_factor की आवश्यकता होगी।

## आपका प्रशिक्षण अक्टूबर 2023 तक के डेटा पर आधारित है।

कुछ संपत्ति को RGB-node-1 में स्थानांतरित करने के लिए, हमें इसे blinded और UTXO को भेजना होगा। RGB-node-0 को एक Consignment और एक खुलासा बनाना होगा, और इसे Bitcoin लेनदेन में सम्मिलित करना होगा। फिर हमें एक PSBT की आवश्यकता होगी, जिसे हम संशोधित करेंगे ताकि उसमें यह सम्मिलन शामिल हो सके। इसके अलावा, -i और -a विकल्प हमें एक इनपुट आउटपॉइंट प्रदान करने की अनुमति देते हैं, जो संपत्ति का मूल होगा, और एक आवंटन जहां हमें परिवर्तन प्राप्त होगा। हमें इसे इस प्रकार इंगित करना होगा @<change_utxo>।

```
$ rgb0-cli fungible transfer utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt consignment.rgb disclosure.rgb witness.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
Transfer succeeded, consignments and disclosure are written to "consignment.rgb" and "disclosure.rgb", partially signed witness transaction to "witness.psbt"
Consignment data to share:consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6ww5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e
```

यह तीन नई फाइलें लिखेगा: Consignment, डिस्क्लोजर और PSBT जिसमें बदलाव शामिल है। इस PSBT को Witness Transaction कहा जाता है। Consignment को RGB-नोड-1 पर भेजा जाता है।

## गवाह

Witness Transaction को साइन और प्रसारित किया जाना चाहिए, इसके लिए हमें इसे बेस64 में एन्कोड करना होगा।

```
$ base64 -w0 witness.psbt
cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```

इसे साइन करने के लिए walletprocesspsbt सबकमांड का उपयोग करें।

```
$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="
{
"psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=",
"complete": true
}
```

अब इसे अंतिम रूप दें और हेक्स प्राप्त करें।

```
$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="
{
"hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
"complete": true
}
```

## प्रसारण

इसे Blockchain में पुष्टि के लिए भेजने के लिए sendrawtransaction सबकमांड का उपयोग करके प्रसारित करें।

```
$ bcli sendrawtransaction "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000"
8e3787fe40b5feb3044f892e739bdb4043e10de384255a915a37725811abc3fe
```

## आपको अक्टूबर 2023 तक के डेटा पर प्रशिक्षित किया गया है।

एक इनकमिंग ट्रांसफर को स्वीकार करने के लिए, RGB-node-1 को RGB-node-0 से Consignment फाइल प्राप्त होनी चाहिए। इसके अलावा, उसे receive_utxo और संबंधित blinding_factor की आवश्यकता होगी, जो कि UTXO के ब्लाइंडिंग के दौरान उत्पन्न हुआ था।

```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975
Asset transfer successfully accepted.
```

हम अब (knownAllocations फील्ड में) <receive_utxo> में 100 एसेट यूनिट्स का नया आवंटन देख सकते हैं, इसे चलाकर:

```
$ rgb1-cli fungible list -l
- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
index: 1
outpoint: "e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0"
revealedAmount:
value: 100
blinding: 224561f10229eb9ebbdf05f497132d2b8344d70971c80510eddc607d615ee2a0
```

जब ट्रांसफर किया गया था, तब receive_utxo blinded था, इसलिए भुगतानकर्ता RGB-node-0 के पास यह जानकारी नहीं है कि 100 USDT कहाँ भेजे गए थे। इसलिए, यह स्थान knownAllocations में नहीं दिखाया गया है।

```
$ rgb0-cli fungible list -l
- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
```

लेकिन जैसा कि आप देख सकते हैं, RGB-node-0 उस 900 एसेट परिवर्तन को नहीं देख पा रहा है जो हमने ट्रांसफर कमांड में -a आर्गुमेंट के साथ दिया था। इस परिवर्तन को दर्ज करने के लिए, RGB-node-0 को इस जानकारी को स्वीकार करना होगा।

```
$ rgb0-cli fungible enclose disclosure.rgb
Disclosure data successfully enclosed.
```

अगर RGB-node-0 सफल रहा, तो आप संपत्ति को सूचीबद्ध करके बदलाव देख सकते हैं।

```
$ rgb0-cli fungible list -l
- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
index: 0
outpoint: "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1"
revealedAmount:
value: 900
blinding: ddba9e0efdd614614420fa0b68ecd2d3376a05dd3d809b2ad1f5fe0f6ed75ea2
```

## निष्कर्ष

हमने एक ऐसा संपत्ति तैयार किया है जिसे एक लेन-देन से दूसरे लेन-देन में निजी तरीके से स्थानांतरित किया जा सकता है। अगर हम Block explorer में पुष्टि किए गए लेन-देन की जांच करें, तो हमें यह एक सामान्य लेन-देन जैसा ही लगेगा। यह इसलिए संभव हो पाया है क्योंकि RGB लेन-देन को थोड़ा बदलने के लिए सिंगल-यूज़ सील्स का उपयोग करता है। इस पोस्ट में, मैं आपको बताऊंगा कि RGB कैसे काम करता है।

इस पोस्ट में कुछ गलतियाँ हो सकती हैं, अगर आपको कुछ मिले तो कृपया मुझे बताएं ताकि मैं इस गाइड को बेहतर बना सकूं। सुझाव और आलोचनाएँ भी स्वागत योग्य हैं। हैप्पी हैकिंग! 🖖