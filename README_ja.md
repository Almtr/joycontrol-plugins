# joycontrol-plugins

[English](./README.md) / [日本語](./README_ja.md)

[joycontrol](https://github.com/mart1nro/joycontrol) と [joycontrol-pluginloader](https://github.com/Almtr/joycontrol-pluginloader) を使用した Nintendo Switch 自動化用プラグインです。


## 必要条件

joycontrol と joycontrol-pluginloader のインストール  
詳細: [GitHub - Almtr/joycontrol-pluginloader - README_ja.md](https://github.com/Almtr/joycontrol-pluginloader/blob/master/README_ja.md)


## ダウンロード

```sh
$ git clone https://github.com/Almtr/joycontrol-plugins.git
```

## プラグイン

詳細は、[wiki](https://github.com/Almtr/joycontrol-plugins/wiki) を参照してください。

- サンプルプラグイン
    - サンプル（SamplePlugin）
- テスト用プラグイン
    - ペアリングテスト（ParingController）
    - コントローラーのボタン入力テスト（TestControllerButtons）
    - コントローラーのスティック入力テスト（TestControllerSticks）
- ユーティリティプラグイン
    - Aボタン連打（RepeatA）
    - 簡易マクロ（SimpleMacro）
- ポケモンソード・シールドプラグイン
    - 日付変更バグ（TimeSkipGlitch）
        - ほりだしもの自動購入（BuyBargains）
        - きのみ自動回収（GetBerries）
        - ハネ自動回収（GetFeathers）
        - ワット自動回収（GetWatts）
        - 自動IDくじ（TryLotoID）
        - マックスレイドバトルのポケモン切替え（ChangeRaidPokemon: Created by [Zobio](https://github.com/Zobio)）
    - マックスレイドバトル周回（AutoRaid）
    - あまいミツとふしぎなアメの合成（CombineHoneyAndCandy）
    - 自動タマゴ孵化（HatchEggs）
    - トーナメント周回（LoopBattleTower）
    - バトルタワー周回（LoopTournament）
    - ポケモン自動逃がし（ReleasePokemons）
    - 乱数調整用の日数消費（SkipDays: Created by [Zobio](https://github.com/Zobio)）