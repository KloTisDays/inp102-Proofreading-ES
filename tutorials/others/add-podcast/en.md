---
name: Adding a Podcast to PlanB Network
description: How to add a new podcast to PlanB Network?
---
![image](assets/cover.webp)

Plan ₿'s mission is to provide top-tier educational resources on Bitcoin in as many languages as possible. All content published on the site is open-source and hosted on GitHub, allowing anyone to participate in enriching the platform.

## Adding a Podcast

Are you looking to add a Bitcoin podcast to the Plan ₿ Network site and increase visibility for your show, but don't know how? This tutorial is for you!
![image](assets/en/01.webp)
- First, you need to have a GitHub account. If you don't know how to create one, we have made a detailed tutorial to guide you.

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Go to [the GitHub repository of Plan ₿ dedicated to data](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/podcasts) in the `resources/podcasts/` section:
![image](assets/en/02.webp)
- Click on the top right on the `Add file` button, then on `Create new file`:
![image](assets/03.webp)
- If you have never contributed to the content of PlanB Network before, you will need to create your fork of the original repository. Forking a repository means creating a copy of that repository on your own GitHub account, allowing you to work on the project without affecting the original repository. Click on the `Fork this repository` button:
![image](assets/04.webp)
- You will then arrive at the GitHub editing page:
![image](assets/05.webp)
- Create a folder for your podcast. To do this, in the `Name your file...` box, write the name of your podcast in lowercase with dashes instead of spaces. For example, if your show is called "Super Podcast Bitcoin", you should write `super-podcast-bitcoin`:
![image](assets/06.webp)
- To validate the creation of the folder, simply add a slash after your podcast name in the same box, for example: `super-podcast-bitcoin/`. Adding a slash automatically creates a folder rather than a file:
![image](assets/07.webp)
- In this folder, you will create a first YAML file named `podcast.yml`:
![image](assets/08.webp)
- Fill in this file with information about your podcast using this template:

```yaml
id:
name:
host:
language:
links:
  podcast:
  twitter:
  website:
description: |

tags:
  -
  -
contributors:
  -
```

Here are the details to fill in for each field:

- **id**: A UUID (Universally Unique Identifier) to uniquely identify the tutorial. You can generate it with an online tool. The only constraint is that this UUID must be random, so as not to conflict with another UUID on the platform;
- **`name`**: Indicate the name of your podcast;
- **`host`**: List the names or pseudonyms of the speakers or the host of the podcast. Each name should be separated by a comma;
- **`language`**: Indicate the language code of the language spoken in your podcast. For example, for English, note `en`, for Italian `it`...

- **`links`**: Provide links to your content. You have two options:
	- `podcast`: the link to your podcast,
	- `twitter`: the link to the Twitter profile of the podcast or the organization producing it,
	- `website`: the link to the website of the podcast or the organization producing it.

- **`description`**: Add a short paragraph that describes your podcast. The description must be in the same language as indicated in the `language:` field.

- **`tags`**: Add two tags associated with your podcast. Examples:
    - `bitcoin`
    - `technology`
    - `economy`
    - `education`...

- **`contributors`**: Mention your contributor ID if you have one.

For example, your YAML file could look like this:

```yaml
id: 723f1d84-8713-4666-9f2e-bc936f26a1ee
name: Super Podcast Bitcoin
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: en
links:
  podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
  twitter: https://twitter.com/decouvrebitcoin
  website: https://decouvrebitcoin.fr
description: |
  Super Podcast Bitcoin is a technical LIVE session held once a week on Twitter to delve deep into the Bitcoin protocol, layer two solutions, and all things that blow minds. Our hosts Lounes, Pantamis, Loïc, and Sosthene will answer your questions and offer the most technical show on Bitcoin in the world.

tags:
  - bitcoin
  - technology
contributors:
  - rabbit-hole
```

- Once you have finished making changes to this file, save them by clicking on the `Commit changes...` button:
![image](assets/10.webp)
- Add a title for your changes, as well as a short description:
![image](assets/11.webp)
- Click on the green `Propose changes` button:
![image](assets/12.webp)
- You will then arrive on a page that summarizes all your changes:
![image](assets/13.webp)
- Click on your GitHub profile picture at the top right, then on `Your Repositories`:
![image](assets/14.webp)
- Select your fork of the PlanB Network repository:
![image](assets/15.webp)
- You should see a notification at the top of the window with your new branch. It's probably called `patch-1`. Click on it:
![image](assets/16.webp)
- You are now on your working branch:
![image](assets/17.webp)
- Go back to the `resources/podcast/` folder and select the podcast folder you just created in the previous commit:
![image](assets/18.webp)
- In your podcast folder, click on the `Add file` button, then on `Create new file`:
![image](assets/19.webp)
- Name this new folder `assets` and confirm its creation by adding a slash `/` at the end:
![image](assets/20.webp)
- In this `assets` folder, create a file named `.gitkeep`:
![image](assets/21.webp)
- Click on the `Commit changes...` button:
![image](assets/22.webp)
- Leave the commit title as default, and make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`:
![image](assets/23.webp)
- Return to the `assets` folder:
![image](assets/24.webp)
- Click on the `Add file` button, then on `Upload files`:
![image](assets/25.webp)
- A new page will open. Drag and drop your podcast logo into the area. This image will be displayed on the PlanB Network site:
![image](assets/26.webp)
- Be careful, the image must be square, to best fit our website:
![image](assets/27.webp)
- Once the image is uploaded, verify that the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`:
![image](assets/28.webp)
- Be careful, your image must be named `logo` and must be in `.webp` format. The full file name should therefore be: `logo.webp`:
![image](assets/29.webp)
- Return to your `assets` folder and click on the intermediary file `.gitkeep`:
![image](assets/30.webp)
- Once on the file, click on the three small dots at the top right then on `Delete file`:
![image](assets/31.webp)
- Verify that you are still on the same working branch, then click on the `Commit changes` button:
![image](assets/32.webp)
- Add a title and description to your commit, then click on `Commit changes`:
![image](assets/33.webp)
- Go back to the root of your repository:
![image](assets/34.webp)
- You should see a message indicating that your branch has undergone changes. Click on the `Compare & pull request` button:
![image](assets/35.webp)
- Add a clear title and description to your PR:
![image](assets/36.webp)
- Click on the `Create pull request` button:
![image](assets/37.webp)
Congratulations! Your PR has been successfully created. An administrator will now review it and, if everything is in order, merge it into the main repository of Plan ₿ Network. You should see your podcast appear on the website a few days later.

Please make sure to follow the progress of your PR. An administrator may leave a comment asking for additional information. As long as your PR is not validated, you can view it in the `Pull requests` tab on the PlanB Network GitHub repository:
![image](assets/38.webp)

# Adding More Resource Types

Podcasts are just the beginning! You have the opportunity to participate in producing other types of resources, which are very similar in structure with a few differences. Let's dive right into those!

You may want to have quick overall look before choosing the one you would like the most:
- **Channels**: YouTube channels about bitcoin, directly or indirectly related
- **Newsletters**: Collection of content that you can use for your educational projects
- **Movies and documentaries**: Discover captivating stories and in-depth explorations of Bitcoin evolution and impact

In the following sections, the different file structures for each of the aforementioned resource types will be presented, so that you can create new resources following the same guidelines as for podcasts.

## Add Channels

- This is the empty template of the `channel.yml` file:

```yaml
id:
name:
language:
links:
  channel:
  trailer:
description: |

contributor_names:
  -
tags:
  -
  -
```

- This is an example of how your `channel.yml` file should look like:

```yaml
id: cd639b66-83c8-4a8e-bc5d-a814bdab379b
name: BTC Sessions
language: en
links:
  channel: https://www.youtube.com/@BTCSessions
  trailer: https://youtu.be/-R7TFUr0tzw
description: |
  BTC Sessions is geared towards helping you understand Bitcoin. Get the tutorials on wallets, hardware, security, exchanges and much more, as well as the latest news and industry interviews.
contributor_names:
  - YourGithubUsername
tags:
  - guides
  - user-friendly
  - wallets
```

#### Notes regarding compilation

- The trailer can be identified as the pinned video on the platform (e.g. like on YouTube), the most viewed video or the most famous one. Dear contributor, this is gonna be up to you; we trust your choice between the aforementioned possibilities.

## Add Newsletters

- This is the empty template of the `newsletter.yml` file:

```yaml
id:
title:
author:
publication_date:
level:
link:
  - website:
language:
  -
description: |

contributor_names:
  -
tags:
  -
  -
```

- This is an example of how your `channel.yml` file should look like:

```yaml
id: 32cd5246-ae6a-4d76-9e1d-8a25cb096e39
title: Bitcoin Optech
author: Adam Jonas, David A. Harding, Gloria Zhao, and al.
publication_date: 2018-06-08
level: expert
link:
  - website: https://bitcoinops.org/en/newsletters/
language:
  - en
description: |
  A key initiative from the Bitcoin Operations Technology Group (Optech) that bridges the gap between Bitcoin businesses and open source technology. The newsletter, released weekly, focuses on helping Bitcoin companies implement the most efficient and cost-effective operational practices. A primary focus is optimizing transaction sizes and managing fee costs through better technical implementation. The content covers technical developments, practical workshops, original research, and real-world case studies. What makes this newsletter particularly valuable is its non-profit nature (funded by member companies and seed investors Wences Casares and John Pfeffer) and its commitment to open source - all materials are released under the MIT license. It's especially relevant for engineers and managers at Bitcoin companies who want to stay current with the latest operational best practices and strengthen their connection to the open source community.
contributor_names:
  - YourGithubUsername
tags:
  - technical-analysis
  - business
  - good-practice
```

## Add Movies

- This is the empty template of the `newsletter.yml` file:

```yaml
id:
title:
author:
publication_year:
duration:
links:
  - platform:
  - trailer
language:
description: |

contributor_names:
  -
tags:
  -
  -
```

- This is an example of how your `channel.yml` file should look like:

```yaml
id: 1a95f951-1caa-4fed-96ca-a87c38e1f13a
title: "Bitcoin: The End of Money as We Know It"
author: Torsten Hoffmann
publication_year: 2015
duration: 60
language: en
links:
  platform: https://youtu.be/zpNlG3VtcBM?si=Q0E7Q-UQC5s3Nvlf
  trailer: https://youtu.be/lUF6klWuB38?si=oe7wEodxAbZbD_v1
description: |
  Bitcoin: The End Of Money As We Know It traces the history of money from the
  bartering societies of the ancient world to the trading floors of Wall St. The
  documentary exposes the practices of central banks and the dubious financial
  actors who brought the world to its knees in the last crisis. It highlights the
  Government influence on the money creation process and how it causes inflation.
  Moreover, this film explains how most money we use today is created out of thin
  air by banks when they create debt. Epic in scope, this film examines the
  patterns of technological innovation and questions everything you thought you
  knew about money. Is Bitcoin an alternative to national currencies backed by
  debt? Will Bitcoin and cryptocurrency spark a revolution in how we use money
  peer to peer? Is it a gift to criminals? Or is it the next bubble waiting to
  burst? If you trust in your money just as it is - this film has news for you.
contributor_names:
  - YourGithubUsername
tags:
  - finance
  - historical
  - high-level
```

#### Notes regarding compilation

- Duration is expressed in minutes. It is gonna be rendered on the platform with both hours and minutes.

Thank you very much for your valuable contribution! :)
