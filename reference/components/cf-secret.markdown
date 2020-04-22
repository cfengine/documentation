---
layout: default
title: cf-agent
published: true
sorting: 10
tags: [Components, cf-agent]
keywords: [agent]
---

`cf-secret` encrypts and decrypts files using CFEngine keys.

Files can be encrypted for one or more public keys. A matching private key is required for decryption.

## Command reference ##

[%CFEngine_include_snippet(cf-secret.help, [\s]*--[a-z], ^$)%]

## Example encrypting and decrypting data

First, let's create a file that contains some content we want to encrypt.

```console
> $ cf-secret --help > /tmp/cf-secret.help
```

Next, let's encrypt the file for the public key used by the host. Run the following command to encrypt the file.

```console
> $ sudo cf-secret encrypt /tmp/cf-secret.help \
                   --output /tmp/cf-secret.help.cfsecret \
                   --key /var/cfengine/ppkeys/localhost.pub
```

Then, inspect file. Note the file contains a header that indicates the key digest identifying the public key for which the file was encrypted.

```console
> $ sudo cat /tmp/cf-secret.help.cfsecret
Version: 1.0
Encrypted-for: SHA=0df59dfd5516a0a66aad933871036fa0ad909d251da682a41775d60db092f154

t"��1)Ȫ��w�+�bX<�-�Z)��W�}��AS
                              �#�,v�f�u��M�N���AV�xx��*^D����OJ�����Ϊ˶�NS�2���ߡ~Bh.▒^
��?$䝒0 ��5w��x�y:�!�HQi.��W@�(�%�.M�▒
       $=��h��N��$����84t/����� ��      �vbb��ao��۠�'N�F줛ey,3��]��y�-n`�H��GϦٕ�LI��N�zH�拥��'1_�D��
                                                                                                  :n/��I_��>�8U���V(�u[�_sJ-QHԀ�Ds���L��4!P��מ�~�`i�>F�~+�Q!�@��{U��T>{pTF7΄#�ȎZךfO���\�B��ݷ�L��d��*8��^��p_��֡
����}ڬ��2�5]?�e?�**▒�"�x����Ts�ԭ�`������eP����*_�
s��3cۈ�jG+��4��H��<▒���9�}��9���!��.�Ai#=�����n����?�����C��?4�I"����R�V7"g��▒_����3��UqE��n▒�����h.��e'���D^CX��)S}����O���"���s�'�[ͽ 7�y��$,��5�!�S=0�<�N���8@K�����nK��ص-BJ2 n[�▒vS��(Y�2M�����|�a 7!�3P0��y9~N9�YLg���l�'d���vĖ�QsB��/�$
��xDط���P��I&rB��"G
|E4}��+=�ښ���ς�m�E��86�E͏^�C��~�n֒���>԰x�Ca�pCE�鱋.▒v������
                                 ԩ�m����y�`�Q���F�gHO▒����,�u���:�m���$ ����H������v�4��Ͳ��6���u���7%(S�饓���@kb�ӯ�:.▒����Xʐ�d-�2�6s�&$�2t����t�M��Y��Q���*9
                                                       ��q�<
h1�qj<2W8O��:�T��7غ�ԥ�GN0�o�p&A=���[<����E��k����A�z]r����v�6ţ9�LH�x�&Z�֙ǖ� s@▒h!
�!Փ��?�4���85��AL��>[��/�y=�!��󺾇Hv�m������z�_��N;��W�����       ��#�i�&�G��̌���K��Z�u�
��L�+wb*�����rpN�B�%
```

Finally, decrypt the file.

```console
> $ sudo cf-secret decrypt /tmp/cf-secret.help.cfsecret \
                   --key /var/cfengine/ppkeys/localhost.priv \
                   --output /tmp/cf-secret.help.decrypted

> $ sudo diff /tmp/cf-secret.help /tmp/cf-secret.help.decrypted && echo "No difference" || echo "Difference detected"

No difference
```
