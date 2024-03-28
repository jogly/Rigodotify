import bpy

from rna_prop_ui import rna_idprop_ui_create

from mathutils import Color


def create(obj):  # noqa
    # generated by rigify.utils.write_metarig
    bpy.ops.object.mode_set(mode='EDIT')
    arm = obj.data

    for i in range(6):
        arm.rigify_colors.add()

    arm.rigify_colors[0].name = "Root"
    arm.rigify_colors[0].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[0].normal = Color((0.4353, 0.1843, 0.4157))
    arm.rigify_colors[0].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[0].standard_colors_lock = True
    arm.rigify_colors[1].name = "IK"
    arm.rigify_colors[1].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[1].normal = Color((0.6039, 0.0000, 0.0000))
    arm.rigify_colors[1].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[1].standard_colors_lock = True
    arm.rigify_colors[2].name = "Special"
    arm.rigify_colors[2].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[2].normal = Color((0.9569, 0.7882, 0.0471))
    arm.rigify_colors[2].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[2].standard_colors_lock = True
    arm.rigify_colors[3].name = "Tweak"
    arm.rigify_colors[3].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[3].normal = Color((0.0392, 0.2118, 0.5804))
    arm.rigify_colors[3].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[3].standard_colors_lock = True
    arm.rigify_colors[4].name = "FK"
    arm.rigify_colors[4].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[4].normal = Color((0.1176, 0.5686, 0.0353))
    arm.rigify_colors[4].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[4].standard_colors_lock = True
    arm.rigify_colors[5].name = "Extra"
    arm.rigify_colors[5].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[5].normal = Color((0.9686, 0.2510, 0.0941))
    arm.rigify_colors[5].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[5].standard_colors_lock = True

    bone_collections = {}

    for bcoll in list(arm.collections_all):
        arm.collections.remove(bcoll)

    def add_bone_collection(name, *, parent=None, ui_row=0, ui_title='', sel_set=False, color_set_id=0):
        new_bcoll = arm.collections.new(name, parent=bone_collections.get(parent))
        new_bcoll.rigify_ui_row = ui_row
        new_bcoll.rigify_ui_title = ui_title
        new_bcoll.rigify_sel_set = sel_set
        new_bcoll.rigify_color_set_id = color_set_id
        bone_collections[name] = new_bcoll

    def assign_bone_collections(pose_bone, *coll_names):
        assert not len(pose_bone.bone.collections)
        for name in coll_names:
            bone_collections[name].assign(pose_bone)

    def assign_bone_collection_refs(params, attr_name, *coll_names):
        ref_list = getattr(params, attr_name + '_coll_refs', None)
        if ref_list is not None:
            for name in coll_names:
                ref_list.add().set_collection(bone_collections[name])

    add_bone_collection('Face', ui_row=1, color_set_id=5)
    add_bone_collection('Face (Primary)', ui_row=2, ui_title='(Primary)', color_set_id=2)
    add_bone_collection('Face (Secondary)', ui_row=2, ui_title='(Secondary)', color_set_id=3)
    add_bone_collection('Torso', ui_row=4, color_set_id=3)
    add_bone_collection('Torso (Tweak)', ui_row=5, ui_title='(Tweak)', color_set_id=4)
    add_bone_collection('Fingers', ui_row=7, color_set_id=6)
    add_bone_collection('Fingers (Detail)', ui_row=8, ui_title='(Detail)', color_set_id=5)
    add_bone_collection('Arm.L (IK)', ui_row=10, color_set_id=2)
    add_bone_collection('Arm.L (FK)', ui_row=11, ui_title='(FK)', color_set_id=5)
    add_bone_collection('Arm.L (Tweak)', ui_row=12, ui_title='(Tweak)', color_set_id=4)
    add_bone_collection('Arm.R (IK)', ui_row=10, color_set_id=2)
    add_bone_collection('Arm.R (FK)', ui_row=11, ui_title='(FK)', color_set_id=5)
    add_bone_collection('Arm.R (Tweak)', ui_row=12, ui_title='(Tweak)', color_set_id=4)
    add_bone_collection('Leg.L (IK)', ui_row=14, color_set_id=2)
    add_bone_collection('Leg.L (FK)', ui_row=15, ui_title='(FK)', color_set_id=5)
    add_bone_collection('Leg.L (Tweak)', ui_row=16, ui_title='(Tweak)', color_set_id=4)
    add_bone_collection('Leg.R (IK)', ui_row=14, color_set_id=2)
    add_bone_collection('Leg.R (FK)', ui_row=15, ui_title='(FK)', color_set_id=5)
    add_bone_collection('Leg.R (Tweak)', ui_row=16, ui_title='(Tweak)', color_set_id=4)
    add_bone_collection('Root', ui_row=19, color_set_id=1)

    bones = {}

    bone = arm.edit_bones.new('spine')
    bone.head = 0.0000, 0.1532, 0.2482
    bone.tail = 0.0000, 0.0897, 0.2311
    bone.roll = 0.0000
    bone.use_connect = False
    bones['spine'] = bone.name
    bone = arm.edit_bones.new('spine.001')
    bone.head = 0.0000, 0.0897, 0.2311
    bone.tail = 0.0000, 0.0318, 0.2254
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine']]
    bones['spine.001'] = bone.name
    bone = arm.edit_bones.new('thigh.L')
    bone.head = 0.0310, 0.1140, 0.2349
    bone.tail = 0.0310, 0.1078, 0.1657
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine']]
    bones['thigh.L'] = bone.name
    bone = arm.edit_bones.new('thigh.R')
    bone.head = -0.0310, 0.1140, 0.2349
    bone.tail = -0.0310, 0.1078, 0.1657
    bone.roll = -0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine']]
    bones['thigh.R'] = bone.name
    bone = arm.edit_bones.new('tail')
    bone.head = 0.0000, 0.1711, 0.2436
    bone.tail = -0.0000, 0.3506, 0.2244
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine']]
    bones['tail'] = bone.name
    bone = arm.edit_bones.new('spine.002')
    bone.head = 0.0000, 0.0318, 0.2254
    bone.tail = 0.0000, -0.0602, 0.2255
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.001']]
    bones['spine.002'] = bone.name
    bone = arm.edit_bones.new('shin.L')
    bone.head = 0.0310, 0.1078, 0.1657
    bone.tail = 0.0310, 0.1688, 0.0960
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['thigh.L']]
    bones['shin.L'] = bone.name
    bone = arm.edit_bones.new('shin.R')
    bone.head = -0.0310, 0.1078, 0.1657
    bone.tail = -0.0310, 0.1688, 0.0960
    bone.roll = -0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['thigh.R']]
    bones['shin.R'] = bone.name
    bone = arm.edit_bones.new('tail.001')
    bone.head = -0.0000, 0.3506, 0.2244
    bone.tail = 0.0000, 0.4600, 0.2334
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['tail']]
    bones['tail.001'] = bone.name
    bone = arm.edit_bones.new('spine.003')
    bone.head = 0.0000, -0.0602, 0.2255
    bone.tail = 0.0000, -0.1546, 0.2346
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.002']]
    bones['spine.003'] = bone.name
    bone = arm.edit_bones.new('feet.L')
    bone.head = 0.0310, 0.1688, 0.0960
    bone.tail = 0.0310, 0.1301, 0.0000
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['shin.L']]
    bones['feet.L'] = bone.name
    bone = arm.edit_bones.new('feet.R')
    bone.head = -0.0310, 0.1688, 0.0960
    bone.tail = -0.0310, 0.1301, 0.0000
    bone.roll = -0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['shin.R']]
    bones['feet.R'] = bone.name
    bone = arm.edit_bones.new('tail.002')
    bone.head = 0.0000, 0.4600, 0.2334
    bone.tail = 0.0000, 0.5469, 0.2484
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['tail.001']]
    bones['tail.002'] = bone.name
    bone = arm.edit_bones.new('spine.004')
    bone.head = 0.0000, -0.1546, 0.2346
    bone.tail = 0.0000, -0.1855, 0.2427
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.003']]
    bones['spine.004'] = bone.name
    bone = arm.edit_bones.new('shoulder.L')
    bone.head = 0.0109, -0.1001, 0.2636
    bone.tail = 0.0345, -0.1426, 0.2085
    bone.roll = 1.2755
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.003']]
    bones['shoulder.L'] = bone.name
    bone = arm.edit_bones.new('shoulder.R')
    bone.head = -0.0109, -0.1001, 0.2636
    bone.tail = -0.0345, -0.1426, 0.2085
    bone.roll = -1.2755
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.003']]
    bones['shoulder.R'] = bone.name
    bone = arm.edit_bones.new('toe.L')
    bone.head = 0.0310, 0.1301, 0.0000
    bone.tail = 0.0310, 0.1077, 0.0000
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['feet.L']]
    bones['toe.L'] = bone.name
    bone = arm.edit_bones.new('toe.R')
    bone.head = -0.0310, 0.1301, 0.0000
    bone.tail = -0.0310, 0.1077, 0.0000
    bone.roll = -0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['feet.R']]
    bones['toe.R'] = bone.name
    bone = arm.edit_bones.new('spine.005')
    bone.head = 0.0000, -0.1855, 0.2427
    bone.tail = 0.0000, -0.2934, 0.2426
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.004']]
    bones['spine.005'] = bone.name
    bone = arm.edit_bones.new('upper_arm.L')
    bone.head = 0.0320, -0.1275, 0.2008
    bone.tail = 0.0320, -0.0992, 0.1239
    bone.roll = 3.1028
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['shoulder.L']]
    bones['upper_arm.L'] = bone.name
    bone = arm.edit_bones.new('upper_arm.R')
    bone.head = -0.0320, -0.1275, 0.2008
    bone.tail = -0.0320, -0.0992, 0.1239
    bone.roll = -3.1028
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['shoulder.R']]
    bones['upper_arm.R'] = bone.name
    bone = arm.edit_bones.new('jaw')
    bone.head = 0.0000, -0.2325, 0.2205
    bone.tail = 0.0000, -0.2681, 0.2125
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.005']]
    bones['jaw'] = bone.name
    bone = arm.edit_bones.new('eye.L')
    bone.head = 0.0327, -0.2258, 0.2647
    bone.tail = 0.0507, -0.2378, 0.2884
    bone.roll = 0.8441
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.005']]
    bones['eye.L'] = bone.name
    bone = arm.edit_bones.new('eye.R')
    bone.head = -0.0327, -0.2258, 0.2647
    bone.tail = -0.0507, -0.2378, 0.2884
    bone.roll = -0.8441
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.005']]
    bones['eye.R'] = bone.name
    bone = arm.edit_bones.new('forearm.L')
    bone.head = 0.0320, -0.0992, 0.1239
    bone.tail = 0.0320, -0.1157, 0.0288
    bone.roll = -3.0743
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['upper_arm.L']]
    bones['forearm.L'] = bone.name
    bone = arm.edit_bones.new('forearm.R')
    bone.head = -0.0320, -0.0992, 0.1239
    bone.tail = -0.0320, -0.1157, 0.0288
    bone.roll = 3.0743
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['upper_arm.R']]
    bones['forearm.R'] = bone.name
    bone = arm.edit_bones.new('hands.L')
    bone.head = 0.0320, -0.1157, 0.0288
    bone.tail = 0.0320, -0.1362, 0.0000
    bone.roll = -3.0599
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['forearm.L']]
    bones['hands.L'] = bone.name
    bone = arm.edit_bones.new('hands.R')
    bone.head = -0.0320, -0.1157, 0.0288
    bone.tail = -0.0320, -0.1362, 0.0000
    bone.roll = 3.0599
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['forearm.R']]
    bones['hands.R'] = bone.name
    bone = arm.edit_bones.new('fingers.L')
    bone.head = 0.0320, -0.1362, 0.0000
    bone.tail = 0.0310, -0.1520, 0.0000
    bone.roll = -3.0399
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['hands.L']]
    bones['fingers.L'] = bone.name
    bone = arm.edit_bones.new('fingers.R')
    bone.head = -0.0320, -0.1362, 0.0000
    bone.tail = -0.0310, -0.1520, 0.0000
    bone.roll = 3.0399
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['hands.R']]
    bones['fingers.R'] = bone.name

    bpy.ops.object.mode_set(mode='OBJECT')
    pbone = obj.pose.bones[bones['spine']]
    pbone.rigify_type = 'spines.basic_spine'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Torso')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Torso (Tweak)')
    assign_bone_collection_refs(pbone.rigify_parameters, 'fk', 'Torso (Tweak)')
    pbone = obj.pose.bones[bones['spine.001']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Torso')
    pbone = obj.pose.bones[bones['thigh.L']]
    pbone.rigify_type = 'limbs.paw'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Leg.L (IK)')
    try:
        pbone.rigify_parameters.limb_type = 'leg'
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.extra_ik_toe = True
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.ik_local_location = False
    except AttributeError:
        pass
    assign_bone_collection_refs(pbone.rigify_parameters, 'fk', 'Leg.L (FK)')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Leg.L (Tweak)')
    pbone = obj.pose.bones[bones['thigh.R']]
    pbone.rigify_type = 'limbs.paw'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Leg.R (IK)')
    try:
        pbone.rigify_parameters.limb_type = 'leg'
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.extra_ik_toe = True
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.ik_local_location = False
    except AttributeError:
        pass
    assign_bone_collection_refs(pbone.rigify_parameters, 'fk', 'Leg.R (FK)')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Leg.R (Tweak)')
    pbone = obj.pose.bones[bones['tail']]
    pbone.rigify_type = 'spines.basic_tail'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Face')
    try:
        pbone.rigify_parameters.connect_chain = False
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['spine.002']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Torso')
    pbone = obj.pose.bones[bones['shin.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Leg.L (IK)')
    pbone = obj.pose.bones[bones['shin.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Leg.R (IK)')
    pbone = obj.pose.bones[bones['tail.001']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Face')
    pbone = obj.pose.bones[bones['spine.003']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Torso')
    pbone = obj.pose.bones[bones['feet.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Leg.L (IK)')
    pbone = obj.pose.bones[bones['feet.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Leg.R (IK)')
    pbone = obj.pose.bones[bones['tail.002']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Face')
    pbone = obj.pose.bones[bones['spine.004']]
    pbone.rigify_type = 'spines.super_head'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Torso')
    try:
        pbone.rigify_parameters.connect_chain = True
    except AttributeError:
        pass
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Torso (Tweak)')
    pbone = obj.pose.bones[bones['shoulder.L']]
    pbone.rigify_type = 'basic.super_copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'YXZ'
    assign_bone_collections(pbone, 'Torso')
    try:
        pbone.rigify_parameters.make_widget = True
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.super_copy_widget_type = 'shoulder'
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['shoulder.R']]
    pbone.rigify_type = 'basic.super_copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'YXZ'
    assign_bone_collections(pbone, 'Torso')
    try:
        pbone.rigify_parameters.make_widget = True
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.super_copy_widget_type = 'shoulder'
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['toe.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Leg.L (IK)')
    pbone = obj.pose.bones[bones['toe.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Leg.R (IK)')
    pbone = obj.pose.bones[bones['spine.005']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Torso')
    pbone = obj.pose.bones[bones['upper_arm.L']]
    pbone.rigify_type = 'limbs.paw'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Arm.L (IK)')
    try:
        pbone.rigify_parameters.ik_local_location = False
    except AttributeError:
        pass
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Arm.L (Tweak)')
    assign_bone_collection_refs(pbone.rigify_parameters, 'fk', 'Arm.L (FK)')
    pbone = obj.pose.bones[bones['upper_arm.R']]
    pbone.rigify_type = 'limbs.paw'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Arm.R (IK)')
    try:
        pbone.rigify_parameters.ik_local_location = False
    except AttributeError:
        pass
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Arm.R (Tweak)')
    assign_bone_collection_refs(pbone.rigify_parameters, 'fk', 'Arm.R (FK)')
    pbone = obj.pose.bones[bones['jaw']]
    pbone.rigify_type = 'basic.super_copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Face')
    pbone = obj.pose.bones[bones['eye.L']]
    pbone.rigify_type = 'basic.super_copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Face')
    pbone = obj.pose.bones[bones['eye.R']]
    pbone.rigify_type = 'basic.super_copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Face')
    pbone = obj.pose.bones[bones['forearm.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Arm.L (IK)')
    pbone = obj.pose.bones[bones['forearm.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Arm.R (IK)')
    pbone = obj.pose.bones[bones['hands.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Arm.L (IK)')
    pbone = obj.pose.bones[bones['hands.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Arm.R (IK)')
    pbone = obj.pose.bones[bones['fingers.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    pbone = obj.pose.bones[bones['fingers.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')

    bpy.ops.object.mode_set(mode='EDIT')
    for bone in arm.edit_bones:
        bone.select = False
        bone.select_head = False
        bone.select_tail = False
    for b in bones:
        bone = arm.edit_bones[bones[b]]
        bone.select = True
        bone.select_head = True
        bone.select_tail = True
        bone.bbone_x = bone.bbone_z = bone.length * 0.05
        arm.edit_bones.active = bone

    arm.collections.active_index = 0

    return bones


if __name__ == "__main__":
    create(bpy.context.active_object)
