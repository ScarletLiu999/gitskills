import os

def check_data_consistency(dataset_dir):
    """
    检查数据集目录中 RGB-D 帧数和 traj.txt 行数是否一致。
    :param dataset_dir: 例如 './data/CP-SLAM_dataset/desk_part1'
    """
    results_dir = os.path.join(dataset_dir, 'results')
    traj_path = os.path.join(dataset_dir, 'traj.txt')

    # 检查是否存在
    if not os.path.exists(results_dir):
        print(f"{results_dir} 不存在！")
        return
    if not os.path.exists(traj_path):
        print(f"{traj_path} 不存在！")
        return

    # 统计帧数
    rgb_files = sorted([f for f in os.listdir(results_dir) if f.endswith('.jpg')])
    depth_files = sorted([f for f in os.listdir(results_dir) if f.endswith('.png')])

    rgb_count = len(rgb_files)
    depth_count = len(depth_files)

    # 统计 traj.txt 行数
    with open(traj_path, 'r') as f:
        traj_lines = f.readlines()
    traj_count = len(traj_lines)

    # 打印结果
    print(f"{dataset_dir}:")
    print(f"   - RGB 帧数: {rgb_count}")
    print(f"   - Depth 帧数: {depth_count}")
    print(f"   - Trajectory 行数: {traj_count}")

    # 判断一致性
    if rgb_count == depth_count == traj_count:
        print(f"数据完整一致！")
    else:
        print(f"数据不一致！请手动检查。")

# 示例使用
if __name__ == "__main__":
    # 这里可以列出你想检查的多个数据集路径
    dataset_list = [
        './data/CP-SLAM_dataset/desk_part1',
        './data/CP-SLAM_dataset/desk2_part1'
    ]

    for dataset_dir in dataset_list:
        check_data_consistency(dataset_dir)
