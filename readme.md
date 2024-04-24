# Documentation du projet

## Model


## Serializers Simple
* __*Importation*__
> from rest_framework import ``serializers``\
> from __.models__ import ``Option``
________
* __*Structure de la classe*__
> __class__ `OptionSerializer`(``serializers``.ModelSerializer):\
&emsp;&emsp;class `Meta`:\
> &emsp;&emsp;&emsp;&emsp;model = Option\
> &emsp;&emsp;&emsp;&emsp;# Afficher tous les champs\
> &emsp;&emsp;&emsp;&emsp;fields = '``__all__``'\
> &emsp;&emsp;&emsp;&emsp; # Afficher des champs personalisés\
> &emsp;&emsp;&emsp;&emsp; fields = ['```libelleOption```','```Autrechamps```']


## View