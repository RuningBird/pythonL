import tensorflow as tf

sess = tf.Session()
a = tf.constant(1)
b = tf.constant(2)

c = sess.run(a + b)
print(c)
