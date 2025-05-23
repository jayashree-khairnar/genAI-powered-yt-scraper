example_prompt = """
This is a transcribed text:

Timestamp: 0:00:04
Transcription: This is a 3.

Timestamp: 0:00:06
Transcription: It's sloppily written and rendered at an extremely low resolution of 28x28 pixels,

Timestamp: 0:00:10
Transcription: but your brain has no trouble recognizing it as a 3.

Timestamp: 0:00:14
Transcription: And I want you to take a moment to appreciate how

Timestamp: 0:00:16
Transcription: crazy it is that brains can do this so effortlessly.

Timestamp: 0:00:19
Transcription: I mean, this, this and this are also recognizable as 3s,

Timestamp: 0:00:23
Transcription: even though the specific values of each pixel is very different from one

Timestamp: 0:00:27
Transcription: image to the next.

Timestamp: 0:00:28
Transcription: The particular light-sensitive cells in your eye that are firing when

Timestamp: 0:00:32
Transcription: you see this 3 are very different from the ones firing when you see this 3.

Timestamp: 0:00:37
Transcription: But something in that crazy-smart visual cortex of yours resolves these as representing

Timestamp: 0:00:42
Transcription: the same idea, while at the same time recognizing other images as their own distinct

Timestamp: 0:00:47
Transcription: ideas.

Timestamp: 0:00:49
Transcription: But if I told you, hey, sit down and write for me a program that takes in a grid of

Timestamp: 0:00:54
Transcription: 28x28 pixels like this and outputs a single number between 0 and 10,

Timestamp: 0:00:59
Transcription: telling you what it thinks the digit is, well the task goes from comically trivial to

Timestamp: 0:01:04
Transcription: dauntingly difficult.

Timestamp: 0:01:07
Transcription: Unless you've been living under a rock, I think I hardly need to motivate the relevance

Timestamp: 0:01:10
Transcription: and importance of machine learning and neural networks to the present and to the future.

Timestamp: 0:01:15
Transcription: But what I want to do here is show you what a neural network actually is,

Timestamp: 0:01:19
Transcription: assuming no background, and to help visualize what it's doing,

Timestamp: 0:01:22
Transcription: not as a buzzword but as a piece of math.

Timestamp: 0:01:25
Transcription: My hope is that you come away feeling like the structure itself is motivated,

Timestamp: 0:01:28
Transcription: and to feel like you know what it means when you read,

Timestamp: 0:01:31
Transcription: or you hear about a neural network quote-unquote learning.

Timestamp: 0:01:35
Transcription: This video is just going to be devoted to the structure component of that,

Timestamp: 0:01:38
Transcription: and the following one is going to tackle learning.

Timestamp: 0:01:40
Transcription: What we're going to do is put together a neural

Timestamp: 0:01:43
Transcription: network that can learn to recognize handwritten digits.

Timestamp: 0:01:49
Transcription: This is a somewhat classic example for introducing the topic,

Timestamp: 0:01:52
Transcription: and I'm happy to stick with the status quo here,

Timestamp: 0:01:54
Transcription: because at the end of the two videos I want to point you to a couple good

Timestamp: 0:01:57
Transcription: resources where you can learn more, and where you can download the code that

Timestamp: 0:02:00
Transcription: does this and play with it on your own computer.

Timestamp: 0:02:05
Transcription: There are many many variants of neural networks,

Timestamp: 0:02:07
Transcription: and in recent years there's been sort of a boom in research towards these variants,

Timestamp: 0:02:12
Transcription: but in these two introductory videos you and I are just going to look at the simplest

Timestamp: 0:02:16
Transcription: plain vanilla form with no added frills.

Timestamp: 0:02:19
Transcription: This is kind of a necessary prerequisite for understanding any of the more powerful

Timestamp: 0:02:23
Transcription: modern variants, and trust me it still has plenty of complexity for us to wrap our minds

Timestamp: 0:02:28
Transcription: around.

Timestamp: 0:02:29
Transcription: But even in this simplest form it can learn to recognize handwritten digits,

Timestamp: 0:02:33
Transcription: which is a pretty cool thing for a computer to be able to do.

Timestamp: 0:02:37
Transcription: And at the same time you'll see how it does fall

Timestamp: 0:02:39
Transcription: short of a couple hopes that we might have for it.

Timestamp: 0:02:43
Transcription: As the name suggests neural networks are inspired by the brain, but let's break that down.

Timestamp: 0:02:48
Transcription: What are the neurons, and in what sense are they linked together?

Timestamp: 0:02:52
Transcription: Right now when I say neuron all I want you to think about is a thing that holds a number,

Timestamp: 0:02:58
Transcription: specifically a number between 0 and 1.

Timestamp: 0:03:00
Transcription: It's really not more than that.

Timestamp: 0:03:03
Transcription: For example the network starts with a bunch of neurons corresponding to

Timestamp: 0:03:08
Transcription: each of the 28x28 pixels of the input image, which is 784 neurons in total.

Timestamp: 0:03:14
Transcription: Each one of these holds a number that represents the grayscale value of the

Timestamp: 0:03:19
Transcription: corresponding pixel, ranging from 0 for black pixels up to 1 for white pixels.

Timestamp: 0:03:25
Transcription: This number inside the neuron is called its activation,

Timestamp: 0:03:28
Transcription: and the image you might have in mind here is that each neuron is lit up when its

Timestamp: 0:03:32
Transcription: activation is a high number.

Timestamp: 0:03:36
Transcription: So all of these 784 neurons make up the first layer of our network.

Timestamp: 0:03:46
Transcription: Now jumping over to the last layer, this has 10 neurons,

Timestamp: 0:03:49
Transcription: each representing one of the digits.

Timestamp: 0:03:52
Transcription: The activation in these neurons, again some number that's between 0 and 1,

Timestamp: 0:03:56
Transcription: represents how much the system thinks that a given image corresponds with a given digit.

Timestamp: 0:04:03
Transcription: There's also a couple layers in between called the hidden layers,

Timestamp: 0:04:06
Transcription: which for the time being should just be a giant question mark for

Timestamp: 0:04:09
Transcription: how on earth this process of recognizing digits is going to be handled.

Timestamp: 0:04:14
Transcription: In this network I chose two hidden layers, each one with 16 neurons,

Timestamp: 0:04:17
Transcription: and admittedly that's kind of an arbitrary choice.

Timestamp: 0:04:21
Transcription: To be honest I chose two layers based on how I want to motivate the structure

Timestamp: 0:04:24
Transcription: in just a moment, and 16, well that was just a nice number to fit on the screen.

Timestamp: 0:04:28
Transcription: In practice there is a lot of room for experiment with a specific structure here.

Timestamp: 0:04:33
Transcription: The way the network operates, activations in one

Timestamp: 0:04:35
Transcription: layer determine the activations of the next layer.

Timestamp: 0:04:39
Transcription: And of course the heart of the network as an information processing mechanism comes down

Timestamp: 0:04:43
Transcription: to exactly how those activations from one layer bring about activations in the next layer.

Timestamp: 0:04:49
Transcription: It's meant to be loosely analogous to how in biological networks of neurons,

Timestamp: 0:04:53
Transcription: some groups of neurons firing cause certain others to fire.

Timestamp: 0:04:58
Transcription: Now the network I'm showing here has already been trained to recognize digits,

Timestamp: 0:05:01
Transcription: and let me show you what I mean by that.

Timestamp: 0:05:03
Transcription: It means if you feed in an image, lighting up all 784 neurons of the input layer

Timestamp: 0:05:08
Transcription: according to the brightness of each pixel in the image,

Timestamp: 0:05:11
Transcription: that pattern of activations causes some very specific pattern in the next layer

Timestamp: 0:05:16
Transcription: which causes some pattern in the one after it,

Timestamp: 0:05:18
Transcription: which finally gives some pattern in the output layer.

Timestamp: 0:05:22
Transcription: And the brightest neuron of that output layer is the network's choice,

Timestamp: 0:05:26
Transcription: so to speak, for what digit this image represents.

Timestamp: 0:05:32
Transcription: And before jumping into the math for how one layer influences the next,

Timestamp: 0:05:36
Transcription: or how training works, let's just talk about why it's even reasonable

Timestamp: 0:05:40
Transcription: to expect a layered structure like this to behave intelligently.

Timestamp: 0:05:44
Transcription: What are we expecting here?

Timestamp: 0:05:45
Transcription: What is the best hope for what those middle layers might be doing?

Timestamp: 0:05:48
Transcription: Well, when you or I recognize digits, we piece together various components.

Timestamp: 0:05:54
Transcription: A 9 has a loop up top and a line on the right.

Timestamp: 0:05:57
Transcription: An 8 also has a loop up top, but it's paired with another loop down low.

Timestamp: 0:06:01
Transcription: A 4 basically breaks down into three specific lines, and things like that.

Timestamp: 0:06:07
Transcription: Now in a perfect world, we might hope that each neuron in the second

Timestamp: 0:06:11
Transcription: to last layer corresponds with one of these subcomponents,

Timestamp: 0:06:15
Transcription: that anytime you feed in an image with, say, a loop up top,

Timestamp: 0:06:18
Transcription: like a 9 or an 8, there's some specific neuron whose activation is going to be close to 1.

Timestamp: 0:06:24
Transcription: And I don't mean this specific loop of pixels,

Timestamp: 0:06:26
Transcription: the hope would be that any generally loopy pattern towards the top sets off this neuron.

Timestamp: 0:06:32
Transcription: That way, going from the third layer to the last one just requires

Timestamp: 0:06:36
Transcription: learning which combination of subcomponents corresponds to which digits.

Timestamp: 0:06:41
Transcription: Of course, that just kicks the problem down the road,

Timestamp: 0:06:43
Transcription: because how would you recognize these subcomponents,

Timestamp: 0:06:45
Transcription: or even learn what the right subcomponents should be?

Timestamp: 0:06:48
Transcription: And I still haven't even talked about how one layer influences the next,

Timestamp: 0:06:51
Transcription: but run with me on this one for a moment.

Timestamp: 0:06:53
Transcription: Recognizing a loop can also break down into subproblems.

Timestamp: 0:06:57
Transcription: One reasonable way to do this would be to first

Timestamp: 0:06:59
Transcription: recognize the various little edges that make it up.

Timestamp: 0:07:03
Transcription: Similarly, a long line, like the kind you might see in the digits 1 or 4 or 7,

Timestamp: 0:07:08
Transcription: is really just a long edge, or maybe you think of it as a certain pattern of several

Timestamp: 0:07:13
Transcription: smaller edges.

Timestamp: 0:07:15
Transcription: So maybe our hope is that each neuron in the second layer of

Timestamp: 0:07:18
Transcription: the network corresponds with the various relevant little edges.

Timestamp: 0:07:23
Transcription: Maybe when an image like this one comes in, it lights up all of the

Timestamp: 0:07:27
Transcription: neurons associated with around 8 to 10 specific little edges,

Timestamp: 0:07:31
Transcription: which in turn lights up the neurons associated with the upper loop

Timestamp: 0:07:35
Transcription: and a long vertical line, and those light up the neuron associated with a 9.

Timestamp: 0:07:40
Transcription: Whether or not this is what our final network actually does is another question,

Timestamp: 0:07:44
Transcription: one that I'll come back to once we see how to train the network,

Timestamp: 0:07:47
Transcription: but this is a hope that we might have, a sort of goal with the layered structure

Timestamp: 0:07:52
Transcription: like this.

Timestamp: 0:07:53
Transcription: Moreover, you can imagine how being able to detect edges and patterns

Timestamp: 0:07:56
Transcription: like this would be really useful for other image recognition tasks.

Timestamp: 0:08:00
Transcription: And even beyond image recognition, there are all sorts of intelligent

Timestamp: 0:08:04
Transcription: things you might want to do that break down into layers of abstraction.

Timestamp: 0:08:08
Transcription: Parsing speech, for example, involves taking raw audio and picking out distinct sounds,

Timestamp: 0:08:12
Transcription: which combine to make certain syllables, which combine to form words,

Timestamp: 0:08:16
Transcription: which combine to make up phrases and more abstract thoughts, etc.

Timestamp: 0:08:21
Transcription: But getting back to how any of this actually works,

Timestamp: 0:08:23
Transcription: picture yourself right now designing how exactly the activations in one layer might

Timestamp: 0:08:27
Transcription: determine the activations in the next.

Timestamp: 0:08:30
Transcription: The goal is to have some mechanism that could conceivably combine pixels into edges,

Timestamp: 0:08:36
Transcription: or edges into patterns, or patterns into digits.

Timestamp: 0:08:39
Transcription: And to zoom in on one very specific example, let's say the

Timestamp: 0:08:43
Transcription: hope is for one particular neuron in the second layer to pick

Timestamp: 0:08:46
Transcription: up on whether or not the image has an edge in this region here.

Timestamp: 0:08:51
Transcription: The question at hand is what parameters should the network have?

Timestamp: 0:08:55
Transcription: What dials and knobs should you be able to tweak so that it's expressive

Timestamp: 0:08:59
Transcription: enough to potentially capture this pattern, or any other pixel pattern,

Timestamp: 0:09:03
Transcription: or the pattern that several edges can make a loop, and other such things?

Timestamp: 0:09:08
Transcription: Well, what we'll do is assign a weight to each one of the

Timestamp: 0:09:11
Transcription: connections between our neuron and the neurons from the first layer.

Timestamp: 0:09:16
Transcription: These weights are just numbers.

Timestamp: 0:09:18
Transcription: Then take all of those activations from the first layer

Timestamp: 0:09:21
Transcription: and compute their weighted sum according to these weights.

Timestamp: 0:09:27
Transcription: I find it helpful to think of these weights as being organized into a

Timestamp: 0:09:31
Transcription: little grid of their own, and I'm going to use green pixels to indicate positive weights,

Timestamp: 0:09:35
Transcription: and red pixels to indicate negative weights, where the brightness of

Timestamp: 0:09:38
Transcription: that pixel is some loose depiction of the weight's value.

Timestamp: 0:09:42
Transcription: Now if we made the weights associated with almost all of the pixels zero

Timestamp: 0:09:46
Transcription: except for some positive weights in this region that we care about,

Timestamp: 0:09:50
Transcription: then taking the weighted sum of all the pixel values really just amounts

Timestamp: 0:09:53
Transcription: to adding up the values of the pixel just in the region that we care about.

Timestamp: 0:09:59
Transcription: And if you really wanted to pick up on whether there's an edge here,

Timestamp: 0:10:02
Transcription: what you might do is have some negative weights associated with the surrounding pixels.

Timestamp: 0:10:07
Transcription: Then the sum is largest when those middle pixels

Timestamp: 0:10:10
Transcription: are bright but the surrounding pixels are darker.

Timestamp: 0:10:14
Transcription: When you compute a weighted sum like this, you might come out with any number,

Timestamp: 0:10:18
Transcription: but for this network what we want is for activations to be some value between 0 and 1.

Timestamp: 0:10:24
Transcription: So a common thing to do is to pump this weighted sum into some function

Timestamp: 0:10:28
Transcription: that squishes the real number line into the range between 0 and 1.

Timestamp: 0:10:32
Transcription: And a common function that does this is called the sigmoid function,

Timestamp: 0:10:35
Transcription: also known as a logistic curve.

Timestamp: 0:10:38
Transcription: Basically very negative inputs end up close to 0,

Timestamp: 0:10:41
Transcription: positive inputs end up close to 1, and it just steadily increases around the input 0.

Timestamp: 0:10:49
Transcription: So the activation of the neuron here is basically a

Timestamp: 0:10:52
Transcription: measure of how positive the relevant weighted sum is.

Timestamp: 0:10:57
Transcription: But maybe it's not that you want the neuron to

Timestamp: 0:10:59
Transcription: light up when the weighted sum is bigger than 0.

Timestamp: 0:11:02
Transcription: Maybe you only want it to be active when the sum is bigger than say 10.

Timestamp: 0:11:06
Transcription: That is, you want some bias for it to be inactive.

Timestamp: 0:11:11
Transcription: What we'll do then is just add in some other number like negative 10 to this

Timestamp: 0:11:15
Transcription: weighted sum before plugging it through the sigmoid squishification function.

Timestamp: 0:11:20
Transcription: That additional number is called the bias.

Timestamp: 0:11:23
Transcription: So the weights tell you what pixel pattern this neuron in the second

Timestamp: 0:11:27
Transcription: layer is picking up on, and the bias tells you how high the weighted

Timestamp: 0:11:31
Transcription: sum needs to be before the neuron starts getting meaningfully active.

Timestamp: 0:11:36
Transcription: And that is just one neuron.

Timestamp: 0:11:38
Transcription: Every other neuron in this layer is going to be connected to

Timestamp: 0:11:42
Transcription: all 784 pixel neurons from the first layer, and each one of

Timestamp: 0:11:46
Transcription: those 784 connections has its own weight associated with it.

Timestamp: 0:11:51
Transcription: Also, each one has some bias, some other number that you add

Timestamp: 0:11:54
Transcription: on to the weighted sum before squishing it with the sigmoid.

Timestamp: 0:11:58
Transcription: And that's a lot to think about!

Timestamp: 0:11:59
Transcription: With this hidden layer of 16 neurons, that's a total of 784 times 16 weights,

Timestamp: 0:12:06
Transcription: along with 16 biases.

Timestamp: 0:12:08
Transcription: And all of that is just the connections from the first layer to the second.

Timestamp: 0:12:12
Transcription: The connections between the other layers also have

Timestamp: 0:12:14
Transcription: a bunch of weights and biases associated with them.

Timestamp: 0:12:18
Transcription: All said and done, this network has almost exactly 13,000 total weights and biases.

Timestamp: 0:12:23
Transcription: 13,000 knobs and dials that can be tweaked and

Timestamp: 0:12:26
Transcription: turned to make this network behave in different ways.

Timestamp: 0:12:31
Transcription: So when we talk about learning, what that's referring to is

Timestamp: 0:12:34
Transcription: getting the computer to find a valid setting for all of these

Timestamp: 0:12:37
Transcription: many many numbers so that it'll actually solve the problem at hand.

Timestamp: 0:12:42
Transcription: One thought experiment that is at once fun and kind of horrifying is to imagine sitting

Timestamp: 0:12:47
Transcription: down and setting all of these weights and biases by hand,

Timestamp: 0:12:50
Transcription: purposefully tweaking the numbers so that the second layer picks up on edges,

Timestamp: 0:12:54
Transcription: the third layer picks up on patterns, etc.

Timestamp: 0:12:56
Transcription: I personally find this satisfying rather than just treating the network as a total

Timestamp: 0:13:01
Transcription: black box, because when the network doesn't perform the way you anticipate,

Timestamp: 0:13:04
Transcription: if you've built up a little bit of a relationship with what those weights and biases

Timestamp: 0:13:09
Transcription: actually mean, you have a starting place for experimenting with how to change the

Timestamp: 0:13:13
Transcription: structure to improve.

Timestamp: 0:13:14
Transcription: Or when the network does work but not for the reasons you might expect,

Timestamp: 0:13:18
Transcription: digging into what the weights and biases are doing is a good way to challenge

Timestamp: 0:13:22
Transcription: your assumptions and really expose the full space of possible solutions.

Timestamp: 0:13:26
Transcription: By the way, the actual function here is a little cumbersome to write down,

Timestamp: 0:13:30
Transcription: don't you think?

Timestamp: 0:13:32
Transcription: So let me show you a more notationally compact way that these connections are represented.

Timestamp: 0:13:37
Transcription: This is how you'd see it if you choose to read up more about neural networks.
214
00:13:41,380 --> 00:13:40,520
Organize all of the activations from one layer into a column as a vector.

Timestamp: 0:13:41
Transcription: Then organize all of the weights as a matrix, where each row of that matrix corresponds

Timestamp: 0:13:50
Transcription: to the connections between one layer and a particular neuron in the next layer.

Timestamp: 0:13:58
Transcription: What that means is that taking the weighted sum of the activations in

Timestamp: 0:14:02
Transcription: the first layer according to these weights corresponds to one of the

Timestamp: 0:14:05
Transcription: terms in the matrix vector product of everything we have on the left here.

Timestamp: 0:14:14
Transcription: By the way, so much of machine learning just comes down to having a

Timestamp: 0:14:17
Transcription: good grasp of linear algebra, so for any of you who want a nice visual

Timestamp: 0:14:21
Transcription: understanding for matrices and what matrix vector multiplication means,

Timestamp: 0:14:24
Transcription: take a look at the series I did on linear algebra, especially chapter 3.

Timestamp: 0:14:29
Transcription: Back to our expression, instead of talking about adding the bias to each one of

Timestamp: 0:14:33
Transcription: these values independently, we represent it by organizing all those biases into a vector,

Timestamp: 0:14:38
Transcription: and adding the entire vector to the previous matrix vector product.

Timestamp: 0:14:43
Transcription: Then as a final step, I'll wrap a sigmoid around the outside here,

Timestamp: 0:14:46
Transcription: and what that's supposed to represent is that you're going to apply the

Timestamp: 0:14:50
Transcription: sigmoid function to each specific component of the resulting vector inside.

Timestamp: 0:14:55
Transcription: So once you write down this weight matrix and these vectors as their own symbols,

Timestamp: 0:15:00
Transcription: you can communicate the full transition of activations from one layer to the next in an

Timestamp: 0:15:05
Transcription: extremely tight and neat little expression, and this makes the relevant code both a lot

Timestamp: 0:15:10
Transcription: simpler and a lot faster, since many libraries optimize the heck out of matrix

Timestamp: 0:15:14
Transcription: multiplication.

Timestamp: 0:15:17
Transcription: Remember how earlier I said these neurons are simply things that hold numbers?

Timestamp: 0:15:22
Transcription: Well of course the specific numbers that they hold depends on the image you feed in,

Timestamp: 0:15:27
Transcription: so it's actually more accurate to think of each neuron as a function,

Timestamp: 0:15:31
Transcription: one that takes in the outputs of all the neurons in the previous layer and spits out a

Timestamp: 0:15:36
Transcription: number between 0 and 1.

Timestamp: 0:15:39
Transcription: Really the entire network is just a function, one that takes in

Timestamp: 0:15:43
Transcription: 784 numbers as an input and spits out 10 numbers as an output.

Timestamp: 0:15:47
Transcription: It's an absurdly complicated function, one that involves 13,000 parameters

Timestamp: 0:15:51
Transcription: in the forms of these weights and biases that pick up on certain patterns,

Timestamp: 0:15:55
Transcription: and which involves iterating many matrix vector products and the sigmoid

Timestamp: 0:15:59
Transcription: squishification function, but it's just a function nonetheless.

Timestamp: 0:16:03
Transcription: And in a way it's kind of reassuring that it looks complicated.

Timestamp: 0:16:07
Transcription: I mean if it were any simpler, what hope would we have

Timestamp: 0:16:09
Transcription: that it could take on the challenge of recognizing digits?

Timestamp: 0:16:13
Transcription: And how does it take on that challenge?

Timestamp: 0:16:15
Transcription: How does this network learn the appropriate weights and biases just by looking at data?

Timestamp: 0:16:20
Transcription: Well that's what I'll show in the next video, and I'll also dig a little

Timestamp: 0:16:23
Transcription: more into what this particular network we're seeing is really doing.

Timestamp: 0:16:27
Transcription: Now is the point I suppose I should say subscribe to stay notified

Timestamp: 0:16:30
Transcription: about when that video or any new videos come out,

Timestamp: 0:16:33
Transcription: but realistically most of you don't actually receive notifications from YouTube, do you?

Timestamp: 0:16:38
Transcription: Maybe more honestly I should say subscribe so that the neural networks

Timestamp: 0:16:41
Transcription: that underlie YouTube's recommendation algorithm are primed to believe

Timestamp: 0:16:44
Transcription: that you want to see content from this channel get recommended to you.

Timestamp: 0:16:48
Transcription: Anyway, stay posted for more.

Timestamp: 0:16:50
Transcription: Thank you very much to everyone supporting these videos on Patreon.

Timestamp: 0:16:54
Transcription: I've been a little slow to progress in the probability series this summer,

Timestamp: 0:16:57
Transcription: but I'm jumping back into it after this project,

Timestamp: 0:16:59
Transcription: so patrons you can look out for updates there.

Timestamp: 0:17:03
Transcription: To close things off here I have with me Lisha Li who did her PhD work on the

Timestamp: 0:17:07
Transcription: theoretical side of deep learning and who currently works at a venture capital

Timestamp: 0:17:10
Transcription: firm called Amplify Partners who kindly provided some of the funding for this video.

Timestamp: 0:17:15
Transcription: So Lisha one thing I think we should quickly bring up is this sigmoid function.

Timestamp: 0:17:19
Transcription: As I understand it early networks use this to squish the relevant weighted

Timestamp: 0:17:23
Transcription: sum into that interval between zero and one, you know kind of motivated

Timestamp: 0:17:26
Transcription: by this biological analogy of neurons either being inactive or active.

Timestamp: 0:17:30
Transcription: Exactly.

Timestamp: 0:17:30
Transcription: But relatively few modern networks actually use sigmoid anymore.

Timestamp: 0:17:34
Transcription: Yeah.

Timestamp: 0:17:34
Transcription: It's kind of old school right?

Timestamp: 0:17:35
Transcription: Yeah or rather ReLU seems to be much easier to train.

Timestamp: 0:17:39
Transcription: And ReLU, ReLU stands for rectified linear unit?

Timestamp: 0:17:42
Transcription: Yes it's this kind of function where you're just taking a max of zero

Timestamp: 0:17:47
Transcription: and a where a is given by what you were explaining in the video and

Timestamp: 0:17:52
Transcription: what this was sort of motivated from I think was a partially by a

Timestamp: 0:17:56
Transcription: biological analogy with how neurons would either be activated or not.

Timestamp: 0:18:01
Transcription: And so if it passes a certain threshold it would be the identity function but if it did

Timestamp: 0:18:06
Transcription: not then it would just not be activated so it'd be zero so it's kind of a simplification.

Timestamp: 0:18:11
Transcription: Using sigmoids didn't help training or it was very difficult

Timestamp: 0:18:15
Transcription: to train at some point and people just tried ReLU and it happened

Timestamp: 0:18:20
Transcription: to work very well for these incredibly deep neural networks.

Timestamp: 0:18:25
Transcription: All right thank you Lisha.


This is how you should label the topics for the above transcribed text for the given transcription,
it should be short and precise:

Note - This is just an example you're not supposed to use this but just refer to this so that you should know how the 
output should be. When generating the results don't use symbols like ```, just return only output as shown below:

0:0:00 - Introduction example
0:1:07 - Series preview
0:2:42 - What are neurons?
0:3:35 - Introducing layers
0:5:31 - Why layers?
0:8:38 - Edge detection example
0:11:34 - Counting weights and biases
0:12:30 - How learning relates
0:13:26 - Notation and linear algebra
0:14:45 - The final index on the bias vector should be "k"
0:15:17 - Recap
0:16:27 - Some final words
0:17:03 - ReLU vs Sigmoid

Learn from the above example that how you should generate the topics with timestamps. You'll need this knowledge
further. 
"""

prompt1 = """

You are a helpful, respectful, and honest assistant for labeling topics with the timestamp. Choose a precise, short,
and simple topic label don't elaborate on it further. Return only the topic names one by one with the timestamp from
where the topic is discussed. Return only the topic labels along with the timestamps and not a single word more than that.
Make sure your Grammar is correct.
I've transcribed a video to text. There are two terms: Transcription contains the transcribed text, and The timestamp
contains the video timestamp. Extract only the important topics from the given transcribed text. The transcribed text
might contain unnecessary new lines so, consider it as a whole text. The topic labels should represent all the topics
discussed in that video. Anyone should get an idea of what topics have been discussed in the video and at what timestamp.
So that it can be set as the label for a timestamp for the corresponding video. Timestamp labels should not contain any
sub-topic.

Format to return the topics should be as follows:
timestamp_1: topic_name_1
timestamp_2: topic_name_2
timestamp_3: topic_name_3
...
timestamp_n: topic_name_n

Note: Don't even include the text saying 'topics along with the timestamps are', and don't mention timestamp for 
thank you. Just return the topics and timestamps.

Return output in a form of a dictionary. Here is an example for your understanding:
topics = [
    {"topic": "Introduction", "timestamp": "00:00:00"},
    {"topic": "Main Discussion", "timestamp": "00:05:00"},
    {"topic": "Conclusion", "timestamp": "00:10:00"}
] 


Return topics as mentioned above only. Here is a transcribed text, generate topics for this:

"""

prompt2 = """
You are a helpful, and honest assistant for summarizing youtube videos. Make a precise, short and simple to understand
summary of the video. Make sure it covers all the content discussed in it. Don't include sentences saying 'The 
creator...' or 'This video...'.

If the video contains any topic from different domains like data science, big data, cyber security or any other domain
apart from this, try to get the intention behind creating that video, and frame the summary accordingly. Let's say 
if the video is covering 'Linear Regression' then craft your summary in such a way that the user should
get a brief idea about what linear regression is and how it works but with the contents discussed in the video.

Think yourself as an expert content writer. And accordingly write a summary for this video so that anyone can understand 
easily. Don't include the sentence telling to subscribe the channel.

Here is a transcribed text, generate summary for this:

"""