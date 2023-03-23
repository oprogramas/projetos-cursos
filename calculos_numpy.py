import numpy as np

def calculate(list):

  if len(list) < 9:
    raise TypeError('A lista deve conter nove numeros')

  calculations = {
   'mean': []
  ,'variance': []
  ,'standard deviation': []
  ,'max': []
  ,'min': []
  ,'sum': []
  }

  arr = np.asarray(list)
  shape = arr.reshape(3,3)

  for i in range(2):

    calculations['mean'].append(np.mean(shape, axis=i).tolist())
    calculations['variance'].append(np.var(shape, axis=i).tolist())
    calculations['standard deviation'].append(np.std(shape, axis=i).tolist())
    calculations['min'].append(np.min(shape, axis=i).tolist())
    calculations['max'].append(np.max(shape, axis=i).tolist())
    calculations['sum'].append(np.sum(shape, axis=i).tolist())
    
  calculations['mean'].append(np.mean(shape))
  calculations['variance'].append(np.var(shape))
  calculations['standard deviation'].append(np.std(shape))
  calculations['min'].append(np.min(shape))
  calculations['max'].append(np.max(shape))
  calculations['sum'].append(np.sum(shape))

  return calculations
