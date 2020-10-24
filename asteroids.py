class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        lista = []
        if len(asteroids) <= 1:
            return asteroids
        else:
            for i in range(len(asteroids)):
                if asteroids[i]>0:
                    lista.append(asteroids[i])
                elif len(lista) == 0:
                    lista.append(asteroids[i])
                else:
                    while len(lista) != 0 and asteroids[i] < 0:
                        if lista[-1] == abs(asteroids[i]):
                            lista.pop(-1)
                            break
                        elif lista[-1] < 0 and asteroids[i] < 0:
                            lista.append(asteroids[i])
                            break
                        elif lista[-1] < abs(asteroids[i]):
                            lista.pop(-1)
                            lista.append(asteroids[i])
                            break
                        elif lista[-1] > abs(asteroids[i]):
                            break

            for x in range(len(lista)*2):
                for i in range(len(lista)-1):
                    if lista[i]> 0 and lista[i+1] < 0:
                        if lista[i] > abs(lista[i+1]):
                            lista.pop(i+1)
                            break


                        if lista[i] == abs(lista[i+1]):
                            lista.pop(i)
                            lista.pop(i)
                            break

                        else:
                            lista.pop(i)
                            break
        return lista
