# -*- coding: utf-8 -*-
u"""Data types used in Brazil."""

import re
import six


class CNPJ(object):
    u"""
    Cadastro Nacional de Pessoas Jurídicas.

    O CNPJ é o número único que identifica uma pessoa jurídica.
    https://pt.wikipedia.org/wiki/Cadastro_Nacional_da_Pessoa_Jur%C3%ADdica

    Crie um novo CNPJ a partir de um inteiro ou string:

    >>> CNPJ()
    <CNPJ: 00.000.000/0000-00>
    >>> CNPJ(58414462000135)
    <CNPJ: 58.414.462/0001-35>
    >>> CNPJ('58414462000135')
    <CNPJ: 58.414.462/0001-35>
    >>> CNPJ('58.414.462/0001-35')
    <CNPJ: 58.414.462/0001-35>
    >>> cnpj = CNPJ(58414462000135)
    >>> cnpj.empty
    False
    >>> cnpj.valid
    True

    Usando a classe CNPJ:

    >>> cnpj
    <CNPJ: 58.414.462/0001-35>
    >>> str(cnpj)
    '58.414.462/0001-35'
    >>> cnpj.format('f')
    '58.414.462/0001-35'
    >>> cnpj.format('r')
    '58414462000135'
    >>> cnpj.extensao
    '0001'
    >>> cnpj.raiz
    '58414462'
    >>> cnpj = CNPJ()
    >>> cnpj.empty
    True
    >>> cnpj.valid
    True
    >>> cnpj
    <CNPJ: 00.000.000/0000-00>
    >>> str(cnpj)
    '00.000.000/0000-00'
    >>> cnpj.format('f')
    '00.000.000/0000-00'
    >>> cnpj.format('r')
    '00000000000000'
    >>> cnpj.extensao
    '0000'
    >>> cnpj.raiz
    '00000000'
    """

    def __init__(self, cnpj=0):
        u"""Inicia um CNPJ."""
        self._cnpj = CNPJ.clean(cnpj)

    @property
    def empty(self):
        u"""Flag indicando que o valor está em branco."""
        return int(self._cnpj) == 0

    @property
    def extensao(self):
        u"""
        Extensão do CNPJ.

        A extensão do CNPJ são os quatro números após a barra que identificam o estabelecimento.
        """
        return self._cnpj[8:12]

    @property
    def raiz(self):
        u"""
        Raiz do CNPJ.

        A raiz do CNPJ são os primeiros números que identificam a empresa.
        """
        return self._cnpj[:8]

    @property
    def valid(self):
        u"""Flag indicando que o valor está válido."""
        return CNPJ.validate(self._cnpj)

    def format(self, format_spec='f'):
        u"""
        Formata o CNPJ.

        Códigos de formatação:
        r -> raw
        f -> formatado

        >>> cnpj = CNPJ(58414462000135)
        >>> cnpj.format('r')
        '58414462000135'
        >>> cnpj.format('f')
        '58.414.462/0001-35'
        """
        if format_spec == '' or format_spec == 'f':
            cnpj = CNPJ.clean(self._cnpj)
            return '{0}.{1}.{2}/{3}-{4}'.format(cnpj[0:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:14])
        if format_spec == 'r':
            return self._cnpj
        raise ValueError(
            "Unknown format code '{0}' for object of type '{1}'".format(format_spec, CNPJ.__name__))

    @classmethod
    def clean(cls, cnpj):
        u"""
        Retorna apenas os dígitos do CNPJ.

        >>> CNPJ.clean('58.414.462/0001-35')
        '58414462000135'
        """
        if isinstance(cnpj, six.string_types):
            cnpj = int(re.sub('[^0-9]', '', cnpj))

        return '{0:014d}'.format(cnpj)

    @classmethod
    def validate(cls, cnpj):
        u"""
        Válida o CNPJ.

        >>> CNPJ.validate(58414462000135)
        True
        >>> CNPJ.validate(58414462000136)
        False
        >>> CNPJ.validate('58414462000135')
        True
        >>> CNPJ.validate('58.414.462/0001-35')
        True
        """
        if cnpj is None:
            return False

        digitos_validacao = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        cnpj = CNPJ.clean(cnpj)

        def mod11(value):
            value = value % 11
            return 11 - value if value > 1 else 0

        dig1 = mod11(sum([digitos_validacao[i] * int(cnpj[i - 1]) for i in range(1, 13)]))
        dig2 = mod11(sum([digitos_validacao[i] * int(cnpj[i]) for i in range(0, 13)]))

        return cnpj[-2:] == '{0}{1}'.format(dig1, dig2)

    def __format__(self, format_spec):
        u"""
        Formata o CNPJ.

        Códigos de formatação:
        r -> raw
        f -> formatado

        >>> cnpj = CNPJ(58414462000135)
        >>> '{0} {0:r} {0:f}'.format(cnpj)
        '58.414.462/0001-35 58414462000135 58.414.462/0001-35'
        """
        return self.format(format_spec)

    def __repr__(self):
        u"""Reprentação do CNPJ."""
        return '<CNPJ: {0:f}>'.format(self)

    def __str__(self):
        u"""Reprentação do CNPJ em string."""
        return self.format()


class CPF(object):
    u"""
    Cadastro de Pessoas Físicas.

    O CPF é o número único que identifica uma pessoa física.
    https://pt.wikipedia.org/wiki/Cadastro_de_pessoas_f%C3%ADsicas

    Crie um novo CPF a partir de um inteiro ou string:
    >>> CPF()
    <CPF: 000.000.000-00>
    >>> CPF(58119443659)
    <CPF: 581.194.436-59>
    >>> CPF('58119443659')
    <CPF: 581.194.436-59>
    >>> CPF('581.194.436-59')
    <CPF: 581.194.436-59>
    >>> cpf = CPF(58119443659)
    >>> cpf.empty
    False
    >>> cpf.valid
    True
    >>> cpf
    <CPF: 581.194.436-59>
    >>> str(cpf)
    '581.194.436-59'
    >>> cpf.format('f')
    '581.194.436-59'
    >>> cpf.format('r')
    '58119443659'
    >>> cpf = CPF()
    >>> cpf.empty
    True
    >>> cpf.valid
    True
    >>> cpf
    <CPF: 000.000.000-00>
    >>> str(cpf)
    '000.000.000-00'
    >>> cpf.format('f')
    '000.000.000-00'
    >>> cpf.format('r')
    '00000000000'
    """

    def __init__(self, cpf=0):
        u"""Inicia um CPF."""
        self._cpf = CPF.clean(cpf)

    @property
    def empty(self):
        u"""Flag indicando que o valor está em branco."""
        return int(self._cpf) == 0

    @property
    def valid(self):
        u"""Flag indicando que o valor está válido."""
        return CPF.validate(self._cpf)

    def format(self, format_spec='f'):
        u"""
        Formata o CPF.

        Códigos de formatação:
        r -> raw
        f -> formatado

        >>> cpf = CPF(58119443659)
        >>> cpf.format('r')
        '58119443659'
        >>> cpf.format('f')
        '581.194.436-59'
        """
        if format_spec == '' or format_spec == 'f':
            cpf = CPF.clean(self._cpf)
            return '{0}.{1}.{2}-{3}'.format(cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:11])
        if format_spec == 'r':
            return self._cpf
        raise ValueError(
            "Unknown format code '{0}' for object of type '{1}'".format(format_spec, CPF.__name__))

    @classmethod
    def clean(cls, cpf):
        u"""
        Retorna apenas os dígitos do CPF.

        >>> CPF.clean('581.194.436-59')
        '58119443659'
        """
        if isinstance(cpf, six.string_types):
            cpf = int(re.sub('[^0-9]', '', cpf))

        return '{0:011d}'.format(cpf)

    @classmethod
    def validate(cls, cpf):
        u"""
        Válida o CPF.

        >>> CPF.validate(58119443659)
        True
        >>> CPF.validate(58119443650)
        False
        >>> CPF.validate('58119443659')
        True
        >>> CPF.validate('581.194.436-59')
        True
        """
        if cpf is None:
            return False

        cpf = CPF.clean(cpf)

        def mod11(value):
            return (value % 11) % 10

        dig1 = mod11(sum([(i + 1) * int(cpf[i]) for i in range(0, 9)]))
        dig2 = mod11(sum([i * int(cpf[i]) for i in range(1, 10)]))

        return cpf[-2:] == '{0}{1}'.format(dig1, dig2)

    def __format__(self, format_spec):
        u"""
        Formata o CPF.

        Códigos de formatação:
        r -> raw
        f -> formatado

        >>> cpf = CPF(58119443659)
        >>> '{0} {0:r} {0:f}'.format(cpf)
        '581.194.436-59 58119443659 581.194.436-59'
        """
        return self.format(format_spec)

    def __repr__(self):
        u"""Reprentação do CPF."""
        return '<CPF: {0:f}>'.format(self)

    def __str__(self):
        u"""Reprentação do CPF em string."""
        return self.format()
