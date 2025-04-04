---
name: Developping on Lightning with SDK
goal: 中級RustおよびSDKトレーニングでLightning開発スキルを向上させる。
objectives:
  - Rust言語に慣れる
  - Bitcoin開発にRustを使用する理由を理解する
  - SDKの基礎を習得する
---

# あなたのLN開発スキルを進化させる

SDKを使ったLNの旅へようこそ。

このコースでは、まずRustの基本を学び、次にSDKを使用したLNプログラミングに進み、最後に実践的な演習で締めくくります。様々なバックグラウンドを持つ講師たちが、実践的なスキルへと導き、今日のLNエンジニアがしばしば直面する様々な課題を説明します。

このコースは、2023年10月にトスカーナでFulgur'Venturesによって開催されたLIVEセミナー中に撮影されました。

コースをお楽しみください！

+++

# 導入
<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>

## コースカリキュラム＆導入
<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>

### 導入

SDKに関するこの上級プログラミングコースへようこそ。このトレーニングでは、まずRustの基本を学び、次にBTC＆Rustに焦点を当て、最後にSDKを使用した実践的な演習で締めくくります。

このトレーニングは現在英語のみで提供され、昨年10月にトスカーナでFulgure Ventureによって開催されたライブセミナーの一部でした。LIVEイベントのプログラムは以下にあり、このトレーニングは最初の週のみに焦点を当てます。後半はRGBを対象としており、RGBコースで見ることができます。

### 講師

このプログラムの一部であった講師の皆さんに多大な感謝を:

- Alekos : "こんにちは、私はイタリアのコーダー兼ハッカーです。bitcoindevkit、magicalbitcoin、h4ckbsなど様々なプロジェクトに取り組んできました"
- Andrei : "LIPAのLightning専門家"
- Gabriel : "コードを書いて色々やっています。"
- Jesse de wit : "Lightning networkの熱狂者 | 開発者 | Breez"

### セミナースケジュール

LNトスカーナイベントの第1週
![image](assets/1.webp)

このコースを終えたら、フォローアップトレーニングに興味がある場合は、スケジュールの第2部をこちらでご覧ください:
![image](assets/2.webp)

勉強頑張ってください。

# Rust bookでコードを学ぶ
<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>

## Rustへの導入 (1/7)
<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>
<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>

![video](https://www.youtube.com/watch?v=aZYhDXE_Gas)
:::video id=90b7647a-3072-449a-9308-c4de5b31e6b9:::

## Rustへの導入 (2/7)
<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>

![video](https://youtu.be/Xm8eCv4LQPc)
:::video id=b36a6daa-0d20-4845-955d-85609c59073c:::

## Rustへの導入 (3/7)
<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>

![video](https://youtu.be/R8NeHvHT0uc)
:::video id=4edc57df-84dd-4d42-8ffa-08be94039412:::

## Rustへの導入 (4/7)
<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>

![video](https://youtu.be/et8pKvYiO4c)
:::video id=6f80b98a-8b33-4888-b674-1bbc28c405e9:::

## Rustへの導入 (5/7)
<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>

![video](https://youtu.be/PxQkVmxOc40)
:::video id=ca2a257a-abf3-4eed-adf2-19bd39b91182:::

## Rustへの導入 (6/7)
<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>

![video](https://youtu.be/3C6hl9BW-Ho)
:::video id=664b758a-4459-4c53-ba56-c2d9b03c285e:::

## Rustへの導入 (7/7)
<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>

![video](https://youtu.be/SBDcb_AauHM)
:::video id=95e644d8-f2a6-4850-a5db-508dc5dbece6:::

# Rust & BTC
<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>

## BitcoinにおけるRustの利点
<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>

![video](https://youtu.be/veLj2w6ulpc)
:::video id=2d7caa3a-06e0-415d-96e2-43b175bd87f2:::

## エラーモデル
<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>

![video](https://youtu.be/X3VKhLtKTRU)
:::video id=3f932564-51fa-4175-9080-8c925f7151b2:::

## Unniffit
<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>

![video](https://youtu.be/zro9GQpJrH0)
:::video id=e4a4c8bc-e4ab-42c0-bf08-4e298c02129c:::

## 非同期トレイト
<chapterId>e1610abe-574c-5995-abe4-a92b0dca4c93</chapterId>

![video](https://youtu.be/cz66eTfk0lw)
:::video id=f8f45f03-0f65-42d6-b56c-b5527a8f79ce:::
# SDKを使用したLNP/BPの開発
<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>
## SDK上のLNノード
<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>

![ビデオ](https://youtu.be/aEzpxuhLdeo)

## Breez sdk
<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>

![ビデオ](https://youtu.be/M3ad9BE6ovo)

## lipaのためのGreenlight
<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>

![ビデオ](https://youtu.be/gKiIPF4apeE)

## lipaのためのBreez sdk
<chapterId>93d87d63-dd7b-5e05-ad2e-dda12915ea32</chapterId>

![ビデオ](https://youtu.be/6VaIVvBKjLY)

# まとめ
<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>



## レビュー & 評価
<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>
<isCourseReview>true</isCourseReview>

## まとめ
<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>
<isCourseConclusion>true</isCourseConclusion>