---
name: RGB लाइटनिंग नोड
description: RGB संगत लाइटनिंग नोड को RLN के साथ लॉन्च करने के लिए, आपको कुछ स्टेप्स फॉलो करने होंगे। सबसे पहले, सुनिश्चित करें कि आपके पास सभी आवश्यक सॉफ़्टवेयर और हार्डवेयर हैं। फिर, अपने सिस्टम पर RGB और RLN सॉफ़्टवेयर इंस्टॉल करें। इसके बाद, नेटवर्क सेटअप करें और सुनिश्चित करें कि आपका नोड सही तरीके से कनेक्ट हो रहा है। अंत में, नोड को कॉन्फ़िगर करें और उसे लॉन्च करें। अगर आपको किसी भी स्टेप में दिक्कत आती है, तो संबंधित दस्तावेज़ या ऑनलाइन ट्यूटोरियल्स की मदद लें।
---
![cover](assets/cover.webp)

इस चरण-दर-चरण ट्यूटोरियल में, आप सीखेंगे कि Regtest वातावरण पर एक Lightning RGB नोड कैसे सेट अप करें। हम देखेंगे कि RGB टोकन कैसे बनाएं और उन्हें चैनलों में कैसे प्रसारित करें।

## आरएलएन परियोजना

बिटफिनेक्स की RGB टीम 2022 से RGB इकोसिस्टम को समृद्ध करने के लिए एक पूरी तकनीकी स्टैक विकसित करने पर काम कर रही है। उनका लक्ष्य किसी एक व्यावसायिक उत्पाद को बनाने के बजाय, ओपन-सोर्स सॉफ्टवेयर के टुकड़े उपलब्ध कराने, RGB प्रोटोकॉल विनिर्देशों में योगदान देने और कार्यान्वयन संदर्भ बनाने पर केंद्रित है।

Bitfinex का RGB इकोसिस्टम में एक महत्वपूर्ण योगदान *RGBlib* लाइब्रेरी है। यह Rust में लिखी गई है और Kotlin और Python के माध्यम से एक्सेस की जा सकती है। यह लाइब्रेरी RGB एप्लिकेशन के विकास को काफी सरल बनाती है क्योंकि यह जटिल सत्यापन और सहभागिता तंत्र को समेटे हुए है।

Bitfinex टीम ने एक RGB मोबाइल Wallet भी डिज़ाइन किया है, जिसे "[*Iris Wallet*](https://iriswallet.com/)" कहा जाता है, जो एंड्रॉइड पर उपलब्ध है। यह Wallet एक RGB प्रॉक्सी सर्वर का उपयोग करता है ताकि off-chain डेटा एक्सचेंज (*consignments*) को आसानी से RGB पर *Client-side Validation* के लिए प्रबंधित किया जा सके।

बिटफिनेक्स ने `RGB-lightning-node` (RLN) प्रोजेक्ट भी विकसित किया है। यह Rust daemon पर आधारित है, जो `Rust-lightning` (LDK) के Fork पर आधारित है, और इसे चैनल में RGB संपत्तियों के अस्तित्व को ध्यान में रखते हुए संशोधित किया गया है। जब एक चैनल खोला जाता है, तो RGB टोकन की उपस्थिति को निर्दिष्ट किया जा सकता है, और हर बार जब चैनल की स्थिति अपडेट होती है, तो एक State Transition बनाया जाता है जो लाइटनिंग आउटपुट में टोकनों के वितरण को दर्शाता है। इससे सक्षम होता है:


- यूएसडीटी में लाइटनिंग चैनल खोलें, उदाहरण के लिए;
- इन टोकनों को नेटवर्क के माध्यम से भेजें, बशर्ते कि रूटिंग पथों में पर्याप्त तरलता हो।
- बिजली की सजा और समयबंदी के तर्क का बिना किसी बदलाव के उपयोग करें: बस Commitment Transaction के एक अतिरिक्त आउटपुट में Anchor से RGB के परिवर्तन को शामिल करें।

RLN कोड अभी अपने अल्फा चरण में है: हम इसे **रेगटेस्ट** या केवल **Testnet** पर उपयोग करने की सलाह देते हैं।

## RGB प्रोटोकॉल की याद दिलाना

RGB एक प्रोटोकॉल है जो Bitcoin के ऊपर चलता है और Smart contract की कार्यक्षमता और डिजिटल संपत्ति प्रबंधन का अनुकरण करता है, बिना उस Blockchain को ओवरलोड किए जिस पर यह आधारित है। पारंपरिक On-Chain स्मार्ट कॉन्ट्रैक्ट्स (जैसे कि एथेरियम पर) के विपरीत, RGB "*Client-side Validation*" प्रणाली पर निर्भर करता है: अधिकांश डेटा और स्थिति इतिहास केवल शामिल प्रतिभागियों द्वारा ही आदान-प्रदान और संग्रहीत किए जाते हैं, जबकि Bitcoin Blockchain केवल छोटे क्रिप्टोग्राफिक कमिटमेंट्स की मेजबानी करता है (जैसे *Tapret* या *Opret* के माध्यम से)। RGB प्रोटोकॉल में, Bitcoin Blockchain इसलिए केवल एक समय-स्टैम्पिंग सर्वर और Double-spending सुरक्षा प्रणाली के रूप में कार्य करता है।

RGB Contract एक विकासशील राज्य मशीन की तरह संरचित है। यह एक Genesis से शुरू होता है जो प्रारंभिक स्थिति को परिभाषित करता है (उदाहरण के लिए, Supply, टिकर या अन्य मेटाडेटा का वर्णन करता है) जो एक सख्ती से टाइप और संकलित Schema के अनुसार होता है। इसके बाद, राज्य संक्रमण और यदि आवश्यक हो तो राज्य विस्तार लागू किए जाते हैं ताकि इस स्थिति को संशोधित या विस्तारित किया जा सके। प्रत्येक ऑपरेशन, चाहे वह फंगिबल एसेट्स (RGB20) का स्थानांतरण हो या अद्वितीय एसेट्स (RGB21) का निर्माण हो, *सिंगल-यूज़ सील्स* शामिल करता है। ये Bitcoin UTXOs को off-chain राज्यों से जोड़ते हैं और डबल स्पेंडिंग को रोकते हैं, जबकि गोपनीयता और स्केलेबिलिटी सुनिश्चित करते हैं।

RGB प्रोटोकॉल कैसे काम करता है, इसके बारे में अधिक जानने के लिए, मैं आपको यह व्यापक प्रशिक्षण कोर्स लेने की सलाह देता हूँ:

https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7
## RGB संगत लाइटनिंग नोड इंस्टॉलेशन

`RGB-lightning-node` बाइनरी को संकलित और इंस्टॉल करने के लिए, हम सबसे पहले रिपॉजिटरी और उसके सब-मॉड्यूल्स को क्लोन करते हैं, फिर हम इसे चलाते हैं:

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RLN](assets/fr/01.webp)


- `--recurse-submodules` विकल्प आवश्यक सब-डिवाइस (जिसमें `Rust-lightning` का संशोधित संस्करण भी शामिल है) को भी क्लोन करता है।
- `--shallow-submodules` विकल्प क्लोन की गहराई को सीमित करता है ताकि डाउनलोडिंग तेज़ हो सके, लेकिन फिर भी आवश्यक कमिट्स तक पहुंच प्रदान करता है।

प्रोजेक्ट की मुख्य निर्देशिका से, निम्नलिखित कमांड चलाएं ताकि बाइनरी को संकलित और इंस्टॉल किया जा सके:

```bash
cargo install --locked --debug --path .
```

![RLN](assets/fr/02.webp)


- `--locked` यह सुनिश्चित करता है कि निर्भरता के संस्करण का पालन किया जाए;
- `--debug` अनिवार्य नहीं है, लेकिन यह आपकी मदद कर सकता है ध्यान केंद्रित करने में (अगर आप चाहें तो `--release` का उपयोग कर सकते हैं);
- `--path .` का मतलब है कि `cargo install` को वर्तमान डायरेक्टरी से इंस्टॉल करना है।

इस कमांड के अंत में, एक `RGB-lightning-node` नामक executable आपके `$CARGO_HOME/bin/` में उपलब्ध होगा। सुनिश्चित करें कि यह रास्ता आपके `$PATH` में शामिल है ताकि आप किसी भी डायरेक्टरी से इस कमांड को चला सकें।

## पूर्वापेक्षाएँ

काम करने के लिए, `RGB-lightning-node` daemon को निम्नलिखित की उपस्थिति और कॉन्फ़िगरेशन की आवश्यकता होती है:


- `bitcoind`** नोड

प्रत्येक RLN उदाहरण को अपने On-Chain लेन-देन को प्रसारित और मॉनिटर करने के लिए `bitcoind` के साथ संवाद करना होगा। इसके लिए daemon को प्रमाणीकरण (लॉगिन/पासवर्ड) और URL (होस्ट/पोर्ट) प्रदान करना होगा।


- एक इंडेक्सर** (इलेक्ट्रम या एस्प्लोरा)

daemon को On-Chain लेन-देन की सूची बनाने और उन्हें खोजने में सक्षम होना चाहिए, खासकर उस UTXO को ढूंढने के लिए जिस पर कोई संपत्ति जुड़ी हुई है। आपको अपने Electrum सर्वर या Esplora का URL निर्दिष्ट करना होगा।


- RGB** प्रॉक्सी

प्रॉक्सी सर्वर एक घटक है (वैकल्पिक, लेकिन अत्यधिक अनुशंसित) जो लाइटनिंग पीयर्स के बीच Exchange से RGB *माल* को सरल बनाने के लिए होता है। एक बार फिर, एक URL निर्दिष्ट करना आवश्यक है।

जब daemon को API के माध्यम से *अनलॉक* किया जाता है, तो IDs और URLs दर्ज किए जाते हैं।

## रेगटेस्ट लॉन्च

सरल उपयोग के लिए, एक `regtest.sh` स्क्रिप्ट है जो स्वचालित रूप से Docker के माध्यम से कुछ सेवाएँ शुरू करती है: `bitcoind`, `electrs` (इंडेक्सर), `RGB-proxy-server`।

![RLN](assets/fr/03.webp)

यह आपको एक स्थानीय, अलग-थलग, पूर्व-कॉन्फ़िगर किया गया वातावरण शुरू करने की अनुमति देता है। यह प्रत्येक रीबूट पर कंटेनर और डेटा डायरेक्टरी बनाता और नष्ट करता है। हम इसे शुरू करने से शुरू करेंगे:

```bash
./regtest.sh start
```

यह स्क्रिप्ट यह करेगी:


- एक `docker/` डायरेक्टरी बनाएं ताकि उसमें संग्रहित किया जा सके;
- `bitcoind` को रिगटेस्ट में चलाएं, साथ ही इंडेक्सर `electrs` और `RGB-proxy-server` को भी चलाएं।
- जब तक सब कुछ इस्तेमाल के लिए तैयार न हो जाए, तब तक इंतज़ार करें।

![RLN](assets/fr/04.webp)

अब हम कई RLN नोड्स लॉन्च करेंगे। अलग-अलग शेल्स में, उदाहरण के लिए (3 RLN नोड्स लॉन्च करने के लिए) चलाएँ:

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```

![RLN](assets/fr/05.webp)


- `--network regtest` पैरामीटर यह दर्शाता है कि आप regtest कॉन्फ़िगरेशन का उपयोग कर रहे हैं।
- `--daemon-listening-port` यह बताता है कि लाइटनिंग नोड किस REST पोर्ट पर API कॉल्स (JSON) के लिए सुनेगा।
- `--ldk-peer-listening-port` यह निर्धारित करता है कि Lightning P2P किस पोर्ट पर सुनना चाहिए।
- `dataldk0/`, `dataldk1/` ये स्टोरेज डायरेक्टरी के रास्ते हैं (हर नोड अपनी जानकारी अलग से स्टोर करता है)।

अब आप अपने ब्राउज़र से अपने RLN नोड्स पर कमांड्स चला सकते हैं, इसके लिए API का धन्यवाद। खासकर, यहीं पर आप डेमन्स को *अनलॉक* कर सकते हैं। बस अपने नोड्स वाले कंप्यूटर पर एक ब्राउज़र खोलें और यह URL दर्ज करें:

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

किसी नोड को चैनल खोलने के लिए, उसके पास पहले Address पर बिटकॉइन होने चाहिए, जो निम्नलिखित कमांड से जनरेट किया गया हो (उदाहरण के लिए, नोड नंबर 1 के लिए):

```bash
curl -X POST http://localhost:3001/address
```

इसका उत्तर आपको एक Address देगा।

![RLN](assets/fr/06.webp)

`bitcoind` रेगटेस्ट पर, हम कुछ बिटकॉइन माइन करने जा रहे हैं। इसे चलाएँ:

```bash
./regtest.sh mine 101
```

![RLN](assets/fr/07.webp)

ऊपर दिए गए नोड Address पर धनराशि भेजें:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RLN](assets/fr/08.webp)

फिर लेन-देन की पुष्टि करने के लिए एक ब्लॉक माइन करें:

```bash
./regtest.sh mine 1
```

![RLN](assets/fr/09.webp)

## Testnet को बिना Docker के लॉन्च करना

अगर आप एक अधिक वास्तविक स्थिति का परीक्षण करना चाहते हैं, तो आप Testnet पर RLN नोड्स लॉन्च कर सकते हैं, बजाय इसके कि Regtest में करें। आप इन्हें सार्वजनिक सेवाओं या उन सेवाओं की ओर इंगित कर सकते हैं जिन्हें आप नियंत्रित करते हैं।

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

डिफ़ॉल्ट रूप से, अगर कोई कॉन्फ़िगरेशन नहीं मिलता है, तो daemon कोशिश करेगा कि वह :


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- `indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `प्रॉक्सी_एंडपॉइंट`: `rpcs://proxy.iriswallet.com/0.2/json-RPC`

लॉगिन के साथ:


- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`

आप इन Elements को `init`/`unlock` API के माध्यम से भी कस्टमाइज़ कर सकते हैं।

## RGB टोकन जारी करना

टोकन जारी करने के लिए, हम "रंगीन" UTXOs बनाकर शुरू करेंगे:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```

![RLN](assets/fr/10.webp)

आप निश्चित रूप से क्रम को बदल सकते हैं। लेन-देन की पुष्टि करने के लिए, हम एक :

```bash
./regtest.sh mine 1
```

अब हम एक RGB संपत्ति बना सकते हैं। यह कमांड उस संपत्ति के प्रकार और उसके पैरामीटर पर निर्भर करेगा जिसे आप बनाना चाहते हैं। यहाँ मैं एक NIA (*गैर-फुलाने योग्य संपत्ति*) टोकन बना रहा हूँ जिसका नाम "PBN" है और इसमें 1000 यूनिट्स का Supply है। `precision` आपको यूनिट्स की विभाज्यता को परिभाषित करने की अनुमति देता है।

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RLN](assets/fr/11.webp)

इस प्रतिक्रिया में नए बनाए गए संपत्ति का आईडी शामिल है। इस पहचानकर्ता को याद से नोट कर लें। मेरे मामले में, यह है:

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RLN](assets/fr/12.webp)

आप इसे On-Chain में ट्रांसफर कर सकते हैं, या इसे एक लाइटनिंग चैनल में आवंटित कर सकते हैं। यही हम अगले भाग में करने जा रहे हैं।

## एक चैनल खोलना और RGB संपत्ति का हस्तांतरण करना

आपको पहले अपने नोड को Lightning Network पर एक पीयर से जोड़ना होगा, इसके लिए `/connectpeer` कमांड का उपयोग करें। मेरे उदाहरण में, मैं दोनों नोड्स को नियंत्रित करता हूँ। इसलिए मैं इस कमांड का उपयोग करके अपने दूसरे लाइटनिंग नोड की सार्वजनिक कुंजी प्राप्त करूंगा:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

यह कमांड मेरे नोड नंबर 2 की सार्वजनिक कुंजी लौटाती है:

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RLN](assets/fr/13.webp)

अब हम चैनल खोलेंगे, इसके लिए हमें संबंधित संपत्ति (`PBN`) को निर्दिष्ट करना होगा। `/openchannel` कमांड आपको चैनल का आकार सतोशियों में निर्धारित करने और RGB संपत्ति को शामिल करने का विकल्प देता है। यह इस पर निर्भर करता है कि आप क्या बनाना चाहते हैं, लेकिन मेरे मामले में, कमांड इस प्रकार है:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```

यहाँ और अधिक जानकारी प्राप्त करें:


- `peer_pubkey_and_opt_addr`: उस साथी की पहचान जिससे हम जुड़ना चाहते हैं (वह सार्वजनिक कुंजी जो हमने पहले पाई थी);
- `capacity_sat`: चैनल की कुल क्षमता सतोशियों में;
- `push_msat`: जब चैनल खोला जाता है, तो साथी को प्रारंभ में स्थानांतरित की गई राशि मिलीसातोशिस में होती है (यहाँ मैं तुरंत 10,000 Sats स्थानांतरित करता हूँ ताकि वह बाद में RGB स्थानांतरण कर सके);
- `asset_amount`: चैनल में समर्पित किए जाने वाले RGB संपत्तियों की मात्रा;
- `asset_id`: चैनल में शामिल RGB संपत्ति का एक अनोखा पहचानकर्ता।
- `पब्लिक`: यह बताता है कि चैनल को नेटवर्क पर रूटिंग के लिए सार्वजनिक बनाया जाना चाहिए या नहीं।

![RLN](assets/fr/14.webp)

लेन-देन की पुष्टि करने के लिए, 6 ब्लॉक्स की माइनिंग की जाती है।

```bash
./regtest.sh mine 6
```

![RLN](assets/fr/15.webp)

लाइटनिंग चैनल अब खुला है और इसमें नोड नंबर 1 की तरफ 500 `PBN` टोकन हैं। अगर नोड नंबर 2 `PBN` टोकन प्राप्त करना चाहता है, तो उसे generate और Invoice करना होगा। इसे कैसे करना है, यहां बताया गया है:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```

आपको अक्टूबर 2023 तक के डेटा पर प्रशिक्षित किया गया है।


- `amt_msat`: Invoice की राशि मिलीसातोशिस में (न्यूनतम 3000 Sats);
- `expiry_sec`: Invoice की समाप्ति समय सेकंडों में;
- `asset_id`: Invoice से जुड़े RGB संपत्ति का पहचानकर्ता।
- `asset_amount`: इस Invoice के साथ स्थानांतरित किए जाने वाले RGB संपत्ति की मात्रा।

इसके जवाब में, आपको एक RGB Invoice मिलेगा।

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RLN](assets/fr/16.webp)

अब हम इस Invoice का भुगतान पहले नोड से करेंगे, जिसमें `PBN` टोकन के साथ आवश्यक नकद राशि है।

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RLN](assets/fr/17.webp)

भुगतान कर दिया गया है। इसे सत्यापित करने के लिए आप यह कमांड चला सकते हैं:

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RLN](assets/fr/18.webp)

यहाँ बताया गया है कि RGB संपत्तियों को ले जाने के लिए संशोधित एक लाइटनिंग नोड कैसे तैनात करें। यह प्रदर्शन आधारित है:


- आप एक रिगटेस्ट वातावरण (जैसे `./regtest.sh`) या Testnet का उपयोग कर सकते हैं।
- एक लाइटनिंग नोड (`RGB-lightning-node`) जो कि `bitcoind`, एक इंडेक्सर और एक `RGB-proxy-server` पर आधारित है;
- चैनल खोलने/बंद करने, टोकन जारी करने, लाइटनिंग के माध्यम से संपत्तियों का स्थानांतरण आदि के लिए JSON REST APIs की एक श्रृंखला।

इस प्रक्रिया के लिए धन्यवाद:


- लाइटनिंग एंगेजमेंट लेन-देन में एक अतिरिक्त आउटपुट (OP_RETURN या Taproot) शामिल होता है, जिसमें RGB ट्रांज़िशन का एंकरिंग होता है।
- ट्रांसफर बिल्कुल उसी तरह किए जाते हैं जैसे पारंपरिक लाइटनिंग भुगतान होते हैं, लेकिन इसमें एक RGB टोकन जोड़ा जाता है।
- कई RLN नोड्स को आपस में जोड़कर विभिन्न नोड्स के माध्यम से भुगतान का मार्ग और प्रयोग किया जा सकता है, बशर्ते उस मार्ग पर बिटकॉइन और एसेट RGB की पर्याप्त तरलता हो।

अगर आपको यह ट्यूटोरियल उपयोगी लगा, तो मैं बहुत आभारी रहूँगा अगर आप नीचे एक Green अंगूठा दें। कृपया इस लेख को अपने सोशल नेटवर्क्स पर साझा करने के लिए स्वतंत्र महसूस करें। बहुत-बहुत धन्यवाद!

मैं आपको एक और ट्यूटोरियल की सिफारिश करता हूँ जिसमें मैं समझाता हूँ कि LNP/BP एसोसिएशन द्वारा विकसित RGB CLI टूल का उपयोग करके RGB Contract कैसे बनाया जाता है।

https://planb.network/tutorials/node/others/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4