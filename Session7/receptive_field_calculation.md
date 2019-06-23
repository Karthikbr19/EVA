

![jout](/home/sanju/Downloads/jout.png)

![Screenshot from 2019-06-19 11-52-55](/home/sanju/Desktop/Screenshot from 2019-06-19 11-52-55.png)

## I couldn't able to complete this task.. i know this is wrong :(

| Layer Number                        | Input | Output | Receptive Field | jumpIn |
| ----------------------------------- | ----- | ------ | --------------- | ------ |
| Input Channel                       |       |        | 1               | 1      |
| Conv(7*7, padding=1,<br />stride=2) |       | 112    | 8               | 1      |
| Maxpooling(3*3,Stride=2,padding=0)  | 112   | 56     | 12              | 2*1    |
| Conv(3*3,padding=1,stride=1)        | 56    | 56     | 20              | 4      |
| Maxpooling(3*3,Stride=2,padding=0)  | 56    | 28     | 28              | 4      |
| Inception3A                         |       | 28     | 28              | 8      |
| Inception3B                         | 28    | 28     | 28              | 8      |
| Maxpooling(3*3,Stride=2,padding=0)  | 28    | 14     | 37              | 8      |
| Inception4A                         | 14    | 14     | 37              | 16     |
| Inception4B                         | 14    | 14     | 37              | 16     |
| Inception4C                         | 14    | 14     | 37              | 16     |
| Inception4D                         | 14    | 14     | 37              | 16     |
| Inception4E                         | 14    | 14     | 37              | 16     |
| Maxpooling(3*3,Stride=2,padding=0)  | 14    | 7      | 69              | 16     |
| Inception5A                         | 7     | 7      | 69              | 32     |
| Inception5B                         | 7     | 7      | 69              | 32     |
| Avg Pool                            | 7     | 1      | 261             | 32     |
|                                     |       |        |                 | 32     |
|                                     |       |        |                 |        |
|                                     |       |        |                 |        |
|                                     |       |        |                 |        |


