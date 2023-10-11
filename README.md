# HandAirGesture

Using Hand landmarks legacy as well as upgraded solutions provided by Mediapipe to control mouse cursor, credited to Viet Nguyen @uvipen

However trying to apply Upgraded solutions encountered an issue, which will be well-described in from user @rsandler00 comment below:

"Hi,

I am running on a windows machine and need to install tf-models-official (version 2.13) for computer vision purposes (nothing to do w/ TF Text). However, tf-models-official has tensorflow-text as a dependency. Since there is currently no support for tensorflow-text in windows (see here), this is screwing up my whole setup

tf-models-official is a big-tent package with a lot of different unrelated use cases - and currently tensorflow-text is screwing up its use on all Windows machines. This is really a crappy situation that should be remedied.

I propose either tensorflow-text stops being a formal requirement for tf-models-official OR tensorflow-text starts offering windows support again.

(For anyone wondering, I had to install tf-models-official in pip using the --no-deps parameter and then installed each of the other dependencies one-by-one - very hacky solution)

Thanks,
Roman"
