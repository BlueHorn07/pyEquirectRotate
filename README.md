# pyEquirectRotate

`pyEquirectRotate` support equirectangular rotation with pure python codes. 😎 

You can rotate equirectangular images by rotating the surface of a sphere. 🌏

This code supports (yaw, pitch, roll) rotation, described in this [Wikipedia page](https://en.wikipedia.org/wiki/Rotation_matrix#General_rotations).

I wrote the code to be `numpy`-friendly. 😉

- [x] (yaw, pitch, roll) rotation
- [x] inverse rotation
- [x] `numpy`-friendly
- [x] single point rotation

## Quick Start

```
cd src
python demo.py
```


## Code Detail

### class `EquirectRotate`

This is a class that supports equirectangular rotations.

``` python
equirectRot1 = EquirectRotate(h, w, (yaw, pitch, roll))
rotated_image = equirectRot1.rotate(src_image)
```

Once you create an `EquirectRotate` instance, you can **re-use** it when all other images are same image format; height, width, (yaw, pitch, roll)

After rotating and if you want to restore it, use `.setInverse(True)`. It is described in `demo.py` in more detail.

### function `pointRotate`

This is a function that supports a single point rotating on an equirectangular image.

``` python
rotated_point = pointRotate(h, w, i, j, (yaw, pitch, roll))
```

## Further Reading

- Some formulas are inpirsed by Paul Bourke's work. [link](http://paulbourke.net/dome/dualfish2sphere/)
- If you want more awesome omnidirectional python codes, I recommand this repository!
    - [sunset1995/py360convert](https://github.com/sunset1995/py360convert)
        - I've forked this `py360convert`, and add `p2e`, perpective2equirectangular. [BlueHorn07/py360convert](https://github.com/BlueHorn07/py360convert), [`p2e`](https://github.com/BlueHorn07/py360convert#p2ep_img-fov_deg-u_deg-v_deg-out_hw-in_rot_deg0)
- `C/C++` Equirectangular Rotation - [whdlgp/Equirectangular_rotate](https://github.com/whdlgp/Equirectangular_rotate)
    
