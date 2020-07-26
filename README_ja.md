# joycontrol-plugins

[English](./README.md) / [日本語](./README_ja.md)

[joycontrol](https://github.com/mart1nro/joycontrol) と [joycontrol-pluginloader](https://github.com/Almtr/joycontrol-pluginloader) を使用した Nintendo Switch 自動化用プラグインです。


## インストール

1. joycontrol と joycontrol-pluginloader のインストール

    参照: [GitHub - Almtr/joycontrol-pluginloader - README_ja.md](https://github.com/Almtr/joycontrol-pluginloader/blob/master/README_ja.md)

1. joycontrol-plugins のダウンロード

    ```sh
    $ git clone https://github.com/Almtr/joycontrol-plugins.git
    ```

## ポケモンソード・シールドの自動化プラグイン

### 自動卵孵化プラグイン（HatchEggs Plugin）

このプラグインは、自動で最大960個のタマゴを孵化させることができます。

- 必要条件:
    - アップグレードされたロトムバイク
    - まるいおまもり
    - 「ほのおのからだ」の特性を持つポケモン（セキタンザン、シャンデラなど）

- 使い方:
    1. メニューの「ポケモン」アイコンを左上に移動してください。
    1. インターネットから切断してください。
    1. ボックスの中身を空にしてください。
    1. 「ほのおのからだ」の特性を持つポケモン（と1つのタマゴ）をてもちに入れてください。
    1. ワイルドエリアの預かり屋まで移動してください。
    1. スクリプトを実行してください。

        ```sh
        $ sudo joycontrol-pluginloader -r <Switch Bluetooth Mac address> plugins/pokemon-swsh/HatchEggs.py --plugin-options <タマゴのサイクル数> <孵化させたいポケモンの数>
        ```

        30匹のイーブイを孵化させたい場合の例：

        ```sh
        $ sudo joycontrol-pluginloader -r <Switch Bluetooth Mac address> plugins/pokemon-swsh/HatchEggs.py --plugin-options 35 30 
        ```

        タマゴのサイクル数については、[こちら](https://yakkun.com/swsh/zukan/)を参照してください。
        このページで目的のポケモンを検索し、そのポケモンの「タマゴ歩数」の欄にサイクル数が書かれています。


### ポケモン自動逃がし用プラグイン（ReleasePokemons Plugin）

このプラグインは、自動で30匹のポケモンを逃がすことができます。

- 使い方:
    1. 逃がしたいポケモン30匹が入ったボックスを開いてください。
    1. スクリプトを実行してください。

        ```sh
        $ sudo joycontrol-pluginloader -r <Switch Bluetooth Mac address> plugins/pokemon-swsh/ReleasePokemons.py
        ```

### トーナメント自動周回用プラグイン（LoopTournament Plugin）

このプラグインは、自動でトーナメントを周回します。

- 使い方:

    1. 技を1つだけ覚えたポケモン1匹をてもちに入れてください（例：「アイアンヘッド」のみを覚えたザシアン）。
    1. シュートスタジアムの受付前まで移動してください。
    1. スクリプトを実行してください。

        ```sh
        $ sudo joycontrol-pluginloader -r <Switch Bluetooth Mac address> plugins/pokemon-swsh/LoopTournament.py
        ```

- 参考:
    - http://niwaka-syndrome.blog.jp/archives/20509394.html (Japanese)

### バトルタワー自動周回用プラグイン（LoopBattleTower Plugin）

このプラグインは、自動でバトルタワーを周回します。

- 使い方:
    1. バトルタワー用のチームをレンタルしてください（チームID: 0000-0006-15Y4-3R）
    1. レンタルしたチームでシングルバトルに参加してください。
    1. スクリプトを実行してください。

        ```sh
        $ sudo joycontrol-pluginloader -r <Switch Bluetooth Mac address> plugins/pokemon-swsh/LoopBattleTower.py
        ```

- 参考:
    - https://twitter.com/satoon_sugar/status/1208248084653674496 (Japanese)
    - https://twitter.com/satoon_sugar/status/1208253657470226432 (Japanese)