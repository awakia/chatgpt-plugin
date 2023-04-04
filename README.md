# ChatGPTを作る簡単なサンプル

ChatGPTのプラグインが開発できるようになったので、シュンスケさんと話して速攻で作ってみた時のレポジトリ。

https://twitter.com/HaveShun/status/1643132967907389440?s=20

最初ChatGPTで雛形作ってもらって、あとはこっちで手直しした。

デバッグの過程は、以下参照
https://twitter.com/awakia/status/1643163343895822338?s=20

## 動作のさせ方

### ローカルで立ち上げる

poetryを調べて使えるようにする

```
poetry install
poetry run python app.py
```

`http://localhost:5050`にサービスが立ち上がるはず

### ngrokで公開

ngrokを調べて使えるようにする

```
ngrok http 5050
```

公開URLが出力されるはず
e.g. https://524b-2407-c801-6100-3700-94d1-1a4-fe37-bb3e.jp.ngrok.io/

## 作る時の手順

1. 提供するAPIの、OpenAPIのドキュメントを用意 (openapi.yaml)
2. .well-known/ai-plugin.json を用意して、1を参照する
3. 外部からアクセスできるようにホストする。自分は ngrok を利用した
4. Plugin Storeの右下からDevelop your own pluginをクリックしてあとは流れにそう
5. チェックが通ったら、雰囲気で指示するといい感じにやってくれる

何をいうとトリガーされるのかなどはしっかりai-plugin.jsonとopenapi.yamlに書くと良さそう
