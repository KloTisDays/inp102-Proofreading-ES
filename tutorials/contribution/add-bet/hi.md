---
name: शैक्षिक उपकरण जोड़ना
description: PlanB नेटवर्क पर नए शैक्षिक सामग्री कैसे जोड़ें?
---
![event](assets/cover.webp)

PlanB का मिशन है Bitcoin पर अग्रणी शैक्षिक संसाधन प्रदान करना, जितनी भाषाओं में संभव हो सके। साइट पर प्रकाशित सभी सामग्री ओपन-सोर्स है और GitHub पर होस्ट की गई है, जिससे कोई भी व्यक्ति इस प्लेटफॉर्म को समृद्ध बनाने में भाग ले सकता है।

ट्यूटोरियल और प्रशिक्षण के अलावा, PlanB Network Bitcoin पर विविध शैक्षिक सामग्री की एक विशाल लाइब्रेरी भी प्रदान करता है, जो सभी के लिए उपलब्ध है, [BET (Bitcoin Educational Toolkit) सेक्शन में](https://planb.network/resources/bet)। इस डेटाबेस में शैक्षिक पोस्टर, मीम्स, हास्यप्रद प्रचार पोस्टर, तकनीकी आरेख, लोगो और अन्य उपकरण शामिल हैं। इस पहल का उद्देश्य दुनिया भर में Bitcoin सिखाने वाले व्यक्तियों और समुदायों को आवश्यक दृश्य संसाधन प्रदान करके उनका समर्थन करना है।

क्या आप इस डेटाबेस को समृद्ध करने में भाग लेना चाहते हैं, लेकिन नहीं जानते कैसे? यह ट्यूटोरियल आपके लिए है!

यह ज़रूरी है कि साइट पर डाला गया सारा कंटेंट या तो बिना किसी अधिकार के हो या फिर स्रोत फ़ाइल के लाइसेंस का पालन करता हो। साथ ही, PlanB Network पर प्रकाशित सभी दृश्य [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) लाइसेंस के तहत उपलब्ध कराए जाते हैं।

![event](assets/01.webp)


- सबसे पहले, आपके पास GitHub पर एक खाता होना चाहिए। अगर आपको खाता बनाना नहीं आता, तो हमने एक विस्तृत ट्यूटोरियल तैयार किया है जो आपकी मदद करेगा।

https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

- [PlanB के डेटा के लिए समर्पित GitHub रिपॉजिटरी](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/bet) के `resources/bet/` सेक्शन में जाएं:

![event](assets/02.webp)


- ऊपरी दाएँ कोने में `फाइल जोड़ें` बटन पर क्लिक करें, फिर `नई फाइल बनाएं` पर क्लिक करें।

![event](assets/03.webp)


- यदि आपने पहले कभी PlanB Network की सामग्री में योगदान नहीं दिया है, तो आपको मूल रिपॉजिटरी का अपना Fork बनाना होगा। रिपॉजिटरी को फोर्क करना मतलब उस रिपॉजिटरी की एक कॉपी अपने GitHub अकाउंट पर बनाना होता है, जिससे आप प्रोजेक्ट पर काम कर सकते हैं बिना मूल रिपॉजिटरी को प्रभावित किए। `Fork this repository` बटन पर क्लिक करें:

![event](assets/04.webp)


- इसके बाद आप GitHub संपादन पृष्ठ पर पहुँच जाएंगे:

![event](assets/05.webp)


- अपने सामग्री के लिए एक फोल्डर बनाएं। ऐसा करने के लिए, `Name your file...` बॉक्स में अपनी सामग्री का नाम छोटे अक्षरों में लिखें और स्पेस की जगह डैश का उपयोग करें। उदाहरण के लिए, मान लीजिए कि मैं 2048 शब्दों की BIP39 सूची का एक PDF दृश्य जोड़ना चाहता हूँ। तो, मैं अपने फोल्डर का नाम `bip39-wordlist` रखूंगा। ![event](assets/06.webp)
- फोल्डर बनाने की पुष्टि करने के लिए, बस उसी बॉक्स में नाम के बाद एक स्लैश जोड़ें, जैसे: `bip39-wordlist/`। स्लैश जोड़ने से स्वचालित रूप से एक फोल्डर बन जाता है, न कि एक फाइल।

![event](assets/07.webp)


- इस फोल्डर में, आप एक पहला YAML फाइल बनाएंगे जिसका नाम `bet.yml` होगा:

![event](assets/08.webp)


- इस फाइल को अपने विषय से संबंधित जानकारी से भरें, इस टेम्पलेट का उपयोग करते हुए:

```yaml
builder:
type:
links:
download:
view:
- en:
tags:
-
-
contributors:
-
```

यहाँ प्रत्येक फ़ील्ड के लिए भरने के विवरण दिए गए हैं:


- `बिल्डर`**: PlanB नेटवर्क पर अपने संगठन की पहचान बताएं। अगर आपके पास अभी तक आपकी कंपनी के लिए "बिल्डर" पहचानकर्ता नहीं है, तो आप इस ट्यूटोरियल का पालन करके एक बना सकते हैं।

https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d
यदि आपके पास एक नहीं है, तो आप बस अपने नाम, अपने उपनाम, या अपनी कंपनी के नाम का उपयोग कर सकते हैं बिना एक बिल्डर प्रोफ़ाइल बनाए।


- `प्रकार`**: अपने सामग्री की प्रकृति निम्नलिखित दो विकल्पों में से चुनें:
 - `शैक्षिक सामग्री` शैक्षिक सामग्री के लिए।
 - `विज़ुअल कंटेंट` अन्य प्रकार की विविध सामग्री के लिए।
- `लिंक्स`**: अपनी सामग्री के लिए लिंक्स प्रदान करें। आपके पास दो विकल्प हैं:
 - यदि आप अपना कंटेंट सीधे PlanB के GitHub पर होस्ट करने का निर्णय लेते हैं, तो आपको निम्नलिखित चरणों के दौरान इस फाइल में लिंक जोड़ने की आवश्यकता होगी।
 - अगर आपकी सामग्री कहीं और होस्ट की गई है, जैसे कि आपकी व्यक्तिगत वेबसाइट पर, तो यहां संबंधित लिंक दें:
     - `डाउनलोड`: आपके सामग्री को डाउनलोड करने के लिए एक लिंक।
     - `देखें`: आपके सामग्री को देखने के लिए एक लिंक (यह डाउनलोड लिंक के समान हो सकता है)। अगर आपकी सामग्री कई भाषाओं में उपलब्ध है, तो हर भाषा के लिए एक लिंक जोड़ें।
- `टैग्स`**: अपनी सामग्री से जुड़े दो टैग जोड़ें। उदाहरण:
 - आपको अक्टूबर 2023 तक के डेटा पर प्रशिक्षित किया गया है।
 - आपको अक्टूबर 2023 तक के डेटा पर प्रशिक्षित किया गया है।
 - आपको अक्टूबर 2023 तक के डेटा पर प्रशिक्षित किया गया है।
 - आपकी शिक्षा अक्टूबर 2023 तक के डेटा पर आधारित है।
 - मेम...
- `योगदानकर्ता`: यदि आपके पास कोई योगदानकर्ता पहचानकर्ता है, तो उसका उल्लेख करें।

उदाहरण के लिए, आपकी YAML फाइल कुछ इस तरह दिख सकती है:

```yaml
builder: PlanB-Network
type: Educational Content
links:
download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
view:
- In my example, I will leave the links empty for now, as I will add my PDF directly on GitHub:
![event](assets/09.webp)
- Once your modifications to this file are complete, save them by clicking on the `Commit changes...` button:
![event](assets/10.webp)
- Add a title for your modifications, as well as a short description:
![event](assets/11.webp)
- Click on the green `Propose changes` button:
![event](assets/12.webp)
- You will then arrive on a page that summarizes all your changes:
![event](assets/13.webp)
- Click on your GitHub profile picture at the top right, then on `Your Repositories`:
![event](assets/14.webp)
- Select your fork of the PlanB Network repository:
![event](assets/15.webp)
- You should see a notification at the top of the window with your new branch. It is probably called `patch-1`. Click on it:
![event](assets/16.webp)
- You are now on your working branch (**make sure you are on the same branch as your previous modifications, this is important!**):
![event](assets/17.webp)
- Go back to the `resources/bet/` folder and select the folder of your content that you just created in the previous commit:
![event](assets/18.webp)
- In the folder of your content, click on the `Add file` button, then on `Create new file`:
![event](assets/19.webp)
- Name this new folder `assets` and confirm its creation by putting a slash `/` at the end:
![event](assets/20.webp)
- In this `assets` folder, create a file named `.gitkeep`: ![event](assets/21.webp)
- Click on the `Commit changes...` button: ![event](assets/22.webp)
- Leave the commit title as default, and make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/23.webp)
- Return to the `assets` folder: ![event](assets/24.webp)
- Click on the `Add file` button, then on `Upload files`: ![event](assets/25.webp)
- A new page will open. Drag and drop a thumbnail that represents your content into the area. This image will be displayed on the PlanB Network site: ![event](assets/26.webp)
- It can be a preview, a logo, or an icon: ![event](assets/27.webp)
- Once the image is uploaded, make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/28.webp)
- Be careful, your image must be named `logo` and must be in `.webp` format. The full file name should therefore be: `logo.webp`: ![event](assets/29.webp)
- Return to your `assets` folder and click on the intermediary file `.gitkeep`: ![event](assets/30.webp)
- Once on the file, click on the three small dots at the top right then on `Delete file`: ![event](assets/31.webp)
- Make sure you are still on the same working branch, then click on the `Commit changes` button: ![event](assets/32.webp)
- Add a title and a description to your commit, then click on `Commit changes`: ![event](assets/33.webp)
- Return to the folder of your content: ![event](assets/34.webp)
- Click on the `Add file` button, then on `Create new file`: ![event](assets/35.webp)
- Create a new YAML file by naming it with the indicator of your native language. This file will be used for the content description. For example, if I want to write my description in English, I will name this file `en.yml`: ![event](assets/36.webp)
- Fill out this YAML file using this template:
```

name:
description: |
```
- For the `name` key, you can add the name of your content;
- For the `description` key, you simply need to add a short paragraph that describes your content. The description must be in the same language as the file name. You do not need to translate this description into all the supported languages on the site, as the PlanB teams will do so with their model.
For example, here is what your file might look like:
```

name: BIP39 WORDLIST
description: |
आपको अक्टूबर 2023 तक के डेटा पर प्रशिक्षित किया गया है। 2048 अंग्रेज़ी शब्दों की पूरी और क्रमांकित सूची, जो BIP39 शब्दकोश से ली गई है, का उपयोग Mnemonic वाक्यांशों को एन्कोड करने के लिए किया जाता है। इस दस्तावेज़ को एक पृष्ठ पर प्रिंट किया जा सकता है।

```
![event](assets/37.webp)
- Click on the `Commit changes...` button:
![event](assets/38.webp)
- Ensure that the `Commit directly to the patch-1 branch` box is checked, add a title, then click on `Commit changes`:
![event](assets/39.webp)
- Your content folder should now look like this:
![event](assets/40.webp)
---
*If you prefer not to add the content on GitHub and you have already noted the links in the `bet.yml` file during the previous steps, you can skip this section and go directly to the part concerning the creation of the Pull Request.*
- Return to the `/assets` folder:
![event](assets/41.webp)
- Click on the `Add file` button, then on `Upload files`:
![event](assets/42.webp)
- A new page will open. Drag and drop into the area the content you wish to share:
![event](assets/43.webp)
- For example, I added the PDF file of the BIP39 list:
![event](assets/44.webp)
- Once the content is uploaded, ensure that the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`:
![event](assets/45.webp)
- Return to your `/assets` folder and click on the file you just uploaded:
![event](assets/46.webp)
- Retrieve the intermediate URL of your file. For example, in my case, the URL is:
```

मुझे खेद है, मैं सीधे लिंक या दस्तावेज़ नहीं खोल सकता। लेकिन अगर आपको इस दस्तावेज़ के बारे में कोई जानकारी चाहिए या इसमें कुछ खास समझने में मदद चाहिए, तो कृपया बताएं। मैं आपकी मदद करने की पूरी कोशिश करूंगा।

```
- Keep only the last part of the URL from `/resources` onwards:
```

आपको अक्टूबर 2023 तक के डेटा पर प्रशिक्षित किया गया है।

```
- Add to the base of the URL the following information to have the correct link:
```

आपको अक्टूबर 2023 तक के डेटा पर प्रशिक्षित किया गया है।

```