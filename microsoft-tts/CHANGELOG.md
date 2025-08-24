# Changelog

## [1.3.3](https://github.com/hugobloem/wyoming-microsoft-tts/compare/v1.3.2...v1.3.3) (2025-08-23)


### 👷 Continuous Integration

* Add GitHub Actions workflow for package publishing ([3590efb](https://github.com/hugobloem/wyoming-microsoft-tts/commit/3590efb2e8367c36ad9ec4d2f05bb3c9e5fed307))

## [1.3.2](https://github.com/hugobloem/wyoming-microsoft-tts/compare/v1.3.1...v1.3.2) (2025-08-23)


### 🐛 Bugfixes

* improve error handling and logging in transform_voices_files function ([b2e0b90](https://github.com/hugobloem/wyoming-microsoft-tts/commit/b2e0b904733a3a395df5b4dd92859cc258640adc))


### 🏗️ Maintenance

* **deps:** update base image to Python 3.13 in Dockerfile ([cec2d59](https://github.com/hugobloem/wyoming-microsoft-tts/commit/cec2d595faa68052a913466fe022ac394dede97c))
* Migrate to pyproject.toml and enhance CI workflows ([#123](https://github.com/hugobloem/wyoming-microsoft-tts/issues/123)) ([d0242b1](https://github.com/hugobloem/wyoming-microsoft-tts/commit/d0242b105d1d53e41254dbda5defd2183bdc37f8))


### 🎨 Styles

* format ([353b1e4](https://github.com/hugobloem/wyoming-microsoft-tts/commit/353b1e42c3d001e33159699d87758b90bef7315d))

## [1.3.1](https://github.com/hugobloem/wyoming-microsoft-tts/compare/v1.3.0...v1.3.1) (2025-08-21)


### 🐛 Bugfixes

* voice parsing errors for locales with script codes (fixes [#111](https://github.com/hugobloem/wyoming-microsoft-tts/issues/111)) ([#120](https://github.com/hugobloem/wyoming-microsoft-tts/issues/120)) ([b2f02fb](https://github.com/hugobloem/wyoming-microsoft-tts/commit/b2f02fbab62d608d7154375e754f9ec63215d661))


### 🧪 Tests

* Add comprehensive test coverage for voices.json download functionality ([#121](https://github.com/hugobloem/wyoming-microsoft-tts/issues/121)) ([ba0271d](https://github.com/hugobloem/wyoming-microsoft-tts/commit/ba0271d1bf511d9afc0343566708c1bf79ab4c56))


### 🏗️ Maintenance

* **deps:** bump actions/checkout from 4 to 5 ([#118](https://github.com/hugobloem/wyoming-microsoft-tts/issues/118)) ([31deb21](https://github.com/hugobloem/wyoming-microsoft-tts/commit/31deb214e73ba2c3a46a5870debd1117c7492059))

## [1.3.0](https://github.com/hugobloem/wyoming-microsoft-tts/compare/v1.2.1...v1.3.0) (2025-08-07)


### 🚀 Features

* add partial sentence synthesizing support ([#116](https://github.com/hugobloem/wyoming-microsoft-tts/issues/116)) ([caa6183](https://github.com/hugobloem/wyoming-microsoft-tts/commit/caa61839bb13ff69d2c3e263bbfeb70bc0bf59a9))

## [1.2.1](https://github.com/hugobloem/wyoming-microsoft-tts/compare/v1.2.0...v1.2.1) (2025-08-07)


### 📝 Documentation

* update docker compose instructions @DOliana ([33f4c74](https://github.com/hugobloem/wyoming-microsoft-tts/commit/33f4c744c39a94563c45227f37099311f4790e93))


### 🧪 Tests

* only test for 3.13 ([#108](https://github.com/hugobloem/wyoming-microsoft-tts/issues/108)) ([2b0c9b4](https://github.com/hugobloem/wyoming-microsoft-tts/commit/2b0c9b4ab6376c157f8b6d903a0400a5f0b9f092))


### 🏗️ Maintenance

* **deps:** bump azure-cognitiveservices-speech from 1.42.0 to 1.44.0 ([#105](https://github.com/hugobloem/wyoming-microsoft-tts/issues/105)) ([56f034b](https://github.com/hugobloem/wyoming-microsoft-tts/commit/56f034beb5aa8df48fca776659a1c74a5d759b24))
* **deps:** bump azure-cognitiveservices-speech from 1.44.0 to 1.45.0 ([#110](https://github.com/hugobloem/wyoming-microsoft-tts/issues/110)) ([a270a62](https://github.com/hugobloem/wyoming-microsoft-tts/commit/a270a62eed58b4907ed957f622b89d94f5d22275))
* **deps:** bump wyoming from 1.6.0 to 1.7.1 ([#106](https://github.com/hugobloem/wyoming-microsoft-tts/issues/106)) ([8400041](https://github.com/hugobloem/wyoming-microsoft-tts/commit/8400041cc4dc9fe44419bca6586b6d028763c8da))
* **deps:** bump wyoming from 1.7.1 to 1.7.2 ([#114](https://github.com/hugobloem/wyoming-microsoft-tts/issues/114)) ([f6abf28](https://github.com/hugobloem/wyoming-microsoft-tts/commit/f6abf281ab1515da6221627d21b11948e20b2724))
* **deps:** update lxml requirement from &lt;6,&gt;=5 to &gt;=5,&lt;7 ([#107](https://github.com/hugobloem/wyoming-microsoft-tts/issues/107)) ([0e75ae0](https://github.com/hugobloem/wyoming-microsoft-tts/commit/0e75ae0921763100d5617f36b463c2bfa0d2cf16))

## [1.2.0](https://github.com/hugobloem/wyoming-microsoft-tts/compare/v1.1.2...v1.2.0) (2025-02-23)


### 🚀 Features

* support multilingual voices from the secondaryLocaleList ([#99](https://github.com/hugobloem/wyoming-microsoft-tts/issues/99)) ([876c4a5](https://github.com/hugobloem/wyoming-microsoft-tts/commit/876c4a53e4b9f886b84175b83980ad8e3d42ba25))


### 🧪 Tests

* add python 3.13 ([#100](https://github.com/hugobloem/wyoming-microsoft-tts/issues/100)) ([079a1fa](https://github.com/hugobloem/wyoming-microsoft-tts/commit/079a1fa7045218b458d9c6886dc0968abdedb833))

## [1.1.2](https://github.com/hugobloem/wyoming-microsoft-tts/compare/v1.1.1...v1.1.2) (2025-01-29)


### 🏗️ Maintenance

* **deps:** bump azure-cognitiveservices-speech from 1.41.1 to 1.42.0 ([#94](https://github.com/hugobloem/wyoming-microsoft-tts/issues/94)) ([f70c126](https://github.com/hugobloem/wyoming-microsoft-tts/commit/f70c1261c20eb4b689b23a8110112fd1ce10b1c0))
* **deps:** update black requirement from &lt;25,&gt;=24 to >=24,<26 ([#96](https://github.com/hugobloem/wyoming-microsoft-tts/issues/96)) ([051a3fc](https://github.com/hugobloem/wyoming-microsoft-tts/commit/051a3fc9d425af302bb72882e96f9493be4a3526))

## [1.1.1](https://github.com/hugobloem/wyoming-microsoft-tts/compare/v1.1.0...v1.1.1) (2024-11-23)


### 🐛 Bugfixes

* use name of synthesize voice ([#89](https://github.com/hugobloem/wyoming-microsoft-tts/issues/89)) ([3f4a1f8](https://github.com/hugobloem/wyoming-microsoft-tts/commit/3f4a1f854c8048168cce7489547a0846052bce38))

## [1.1.0](https://github.com/hugobloem/wyoming-microsoft-tts/compare/1.0.8...v1.1.0) (2024-11-23)


### 🚀 Features

* add signal handling for graceful shutdown in main execution ([a63a1f4](https://github.com/hugobloem/wyoming-microsoft-tts/commit/a63a1f483395ce3fee8f77b72056041791b347da))
* enhance argument parsing and validation with environment variable support ([a63a1f4](https://github.com/hugobloem/wyoming-microsoft-tts/commit/a63a1f483395ce3fee8f77b72056041791b347da))


### 🐛 Bugfixes

* add exit call for graceful shutdown on stop signal ([#88](https://github.com/hugobloem/wyoming-microsoft-tts/issues/88)) ([b99f441](https://github.com/hugobloem/wyoming-microsoft-tts/commit/b99f441349b3146757c8aeef51d7fa2659963a29))
* add-on button url ([#77](https://github.com/hugobloem/wyoming-microsoft-tts/issues/77)) ([3532cee](https://github.com/hugobloem/wyoming-microsoft-tts/commit/3532ceedf16a5b91898a9c07abc32ea9de6132a3))
* validate and use default voice in event handling ([#82](https://github.com/hugobloem/wyoming-microsoft-tts/issues/82)) ([320a226](https://github.com/hugobloem/wyoming-microsoft-tts/commit/320a226d6be4cae3f758c0d18458579c99a47024))


### 🔨 Code Refactoring

* enhance error handling and logging in voice loading and synthesis processes ([#87](https://github.com/hugobloem/wyoming-microsoft-tts/issues/87)) ([363a46a](https://github.com/hugobloem/wyoming-microsoft-tts/commit/363a46ad35fa4227c5079c794f58e60960458355))


### 👷 Continuous Integration

* add release-please configuration and workflow files ([#83](https://github.com/hugobloem/wyoming-microsoft-tts/issues/83)) ([dd370fc](https://github.com/hugobloem/wyoming-microsoft-tts/commit/dd370fc33df27d7560be11974661201be04fb32e))
* add required packages ([#76](https://github.com/hugobloem/wyoming-microsoft-tts/issues/76)) ([5e89262](https://github.com/hugobloem/wyoming-microsoft-tts/commit/5e8926288fc36055ddf5640181f38ebd940396af))
* enhance Docker image tagging and labeling in release workflow ([#85](https://github.com/hugobloem/wyoming-microsoft-tts/issues/85)) ([88ff459](https://github.com/hugobloem/wyoming-microsoft-tts/commit/88ff459be2818dbeb421c7c905b4ebc4fa1cee3b))
