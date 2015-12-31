
# Live Code Editor Recording Demo

This is a demo for the [Khan Academy CS](https://www.khanacademy.org/computer-programming/) live code editor. If you want to read more about it, head over to the project's [github page](https://github.com/Khan/live-editor/).
The demo uses a local app engine server to save the recordings, translodit for encoding it to mp3, and S3 for storing the audio files.

#### Prerequisites
* google app engine python SDK
* free transloadit.com account (they have a limit of 1GB per free account)
* AWS S3 bucket

#### Setup
1. download the python [app engine sdk](https://cloud.google.com/appengine/downloads)
2. clone this repo
3. create a free account with [transloadit.com](https://www.transloadit.com)
4. in your account, create a new template which should look like this:
```json
{
    "steps": {
        "mp3": {
          "use": ":original",
          "robot": "/audio/encode"
        },
        "export": {
          "use": "mp3",
          "robot": "/s3/store",
          "key": "S3_KEY",
          "secret": "S3_SECRET",
          "bucket": "S3_bucket_name"
        }
    }
}
```
5. in `views/index.html` at lines 107 - 108 add the keys from your transloadit.com account:
    * `transloaditAuthKey`: found [here](https://transloadit.com/accounts/credentials), named Your Auth Key
    * `transloaditTemplate`: found [here](https://transloadit.com/templates)
6. cd into the project's folder, and run
```
gcloud preview app run ./app.yaml
```
7. go to [localhost:8080](http://localhost:8080)
8. hit **Record**
9. the app allows you to record in chunks, for each chunk press **Start new chunk**, **Stop recording chunk**, **Save recording chunk**, and finally **Save Recording** 

The final recording should be more than 15 seconds, it errors out when the audio file is too small.

### How it works

For a deep dive into the components of the LiveEditor, [read this wiki](https://github.com/Khan/live-editor/wiki/How-the-live-editor-works).
You can also watch these talks that the team has given about the editor:
* [John Resig on CodeGenius](https://www.youtube.com/watch?v=H4sSldXv_S4)
* [Pamela Fox at ReactConf](https://youtu.be/EzHsLt9vLbk?t=26m49s)
